# encoding: utf-8
"""
@author: xyliao
@contact: xyliao1993@qq.com
"""
import warnings
from pprint import pprint


class DefaultConfig(object):
    model = 'CharRNN'

    # Dataset.
    txt = 'jay.txt'
    len = 100
    max_vocab = 5000
    # Store result and save models.
    # result_file = 'test.txt'
    # save_file = './checkpoints/'
    save_freq = 30  # save model every N epochs

    # Visualization parameters.
    # vis_dir = './test_vis/'
    plot_freq = 100  # plot in tensorboard every N iterations

    # Model hyperparameters.
    use_gpu = True  # use GPU or not
    ctx = 0  # running on which cuda device
    batch_size = 128  # batch size
    num_workers = 4  # how many workers for loading data
    max_epoch = 5000
    lr = 1e-4  # initial learning rate
    lr_decay = 0.95
    # lr_decay_freq = 10
    weight_decay = 1e-4

    def _parse(self, kwargs):
        for k, v in kwargs.items():
            if not hasattr(self, k):
                warnings.warn("Warning: opt has not attribut %s" % k)
            setattr(self, k, v)

        print('=========user config==========')
        pprint(self._state_dict())
        print('============end===============')

    def _state_dict(self):
        return {k: getattr(self, k) for k, _ in DefaultConfig.__dict__.items()
                if not k.startswith('_')}


opt = DefaultConfig()
