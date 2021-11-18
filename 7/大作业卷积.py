# encoding: utf-8
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, losses, optimizers, Model
# from exam_rnn import MyRNN  # (可以分离写)

batchsz = 128  # 批量大小
total_words = 10000  # 词汇表大小N_vocab
max_review_len = 80  # 句子最大长度s，大于的句子部分将截断，小于的将填充
embedding_len = 100  # 词向量特征长度n
# 加载IMDB 数据集，此处的数据采用数字编码，一个数字代表一个单词
(x_train, y_train), (x_test, y_test) = keras.datasets.imdb.load_data(num_words=total_words)
# 打印输入的形状，标签的形状
print(x_train.shape, len(x_train[0]), y_train.shape)  # (25000,) 218 (25000,)
print(x_test.shape, len(x_test[0]), y_test.shape)  # (25000,) 68 (25000,)



# 截断和填充句子，使得等长，此处长句子保留句子后面的部分，短句子在前面填充
x_train = keras.preprocessing.sequence.pad_sequences(x_train, maxlen=max_review_len)
x_test = keras.preprocessing.sequence.pad_sequences(x_test, maxlen=max_review_len)

# 构建数据集，打散，批量，并丢掉最后一个不够batchsz 的batch
db_train = tf.data.Dataset.from_tensor_slices((x_train, y_train))
db_train = db_train.shuffle(1000).batch(batchsz, drop_remainder=True)
db_test = tf.data.Dataset.from_tensor_slices((x_test, y_test))
db_test = db_test.batch(batchsz, drop_remainder=True)

print('x_train shape:', x_train.shape, tf.reduce_max(y_train), tf.reduce_min(y_train))
# x_train shape: (25000, 80) tf.Tensor(1, shape=(), dtype=int64) tf.Tensor(0, shape=(), dtype=int64)
print('x_test shape:', x_test.shape)
# x_test shape: (25000, 80)


class MyRNN(Model):
    # Cell 方式构建多层网络
    def __init__(self, units):
        super(MyRNN, self).__init__()
        # [b, 64]，构建Cell 初始化状态向量，重复使用
        self.state0 = [tf.zeros([batchsz, units])]  # 128,64
        self.state1 = [tf.zeros([batchsz, units])]  # 128,64
        # 词向量编码 [b, 80] => [b, 80, 100]
        self.embedding = layers.Embedding(total_words, embedding_len, input_length=max_review_len)
        # 构建2 个Cell，使用dropout 技术防止过拟合
        self.rnn_cell0 = layers.SimpleRNNCell(units)# , dropout=0.5)
        self.rnn_cell1 = layers.SimpleRNNCell(units)#, dropout=0.5)
        # 构建分类网络，用于将CELL 的输出特征进行分类，2 分类
        # [b, 80, 100] => [b, 64] => [b, 1]
        self.outlayer = layers.Dense(1)

    def call(self, inputs, training=None):
        x = inputs  # [128, 80]
        # 获取词向量: [128, 80] => [128, 80, 100]
        x = self.embedding(x)
        # 通过2 个RNN CELL,[128, 80, 100] => [128, 64]
        state0 = self.state0
        state1 = self.state1
        for word in tf.unstack(x, axis=1):  # word: [128, 100]
            out0, state0 = self.rnn_cell0(word, state0, training)
            out1, state1 = self.rnn_cell1(out0, state1, training)

        # 末层最后一个输出作为分类网络的输入: [128, 64] => [128, 1]
        x = self.outlayer(out1)
        # 通过激活函数，p(y is pos|x)
        prob = tf.sigmoid(x)
        return prob


def main():
    units = 64  # RNN 状态向量长度n
    epochs = 20  # 训练epochs
    model = MyRNN(units)  # 创建模型
    # 装配
    model.compile(optimizer=optimizers.Adam(0.001),
                  loss=losses.BinaryCrossentropy(), metrics=['accuracy'],
                  experimental_run_tf_function=False)
    # 训练和验证
    model.fit(db_train, epochs=epochs, validation_data=db_test)
    # 测试
    scores = model.evaluate(db_test)
    print("Final test loss and accuracy :", scores)


if __name__ == '__main__':
    main()