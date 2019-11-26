
'''
================================================================================
============================ DATASETS PARAMETERS ===============================
================================================================================

DATASETS_FOLDER: path to the folder with your dataset.

Fill in the datasets infos following the structure
DATASETS = [
    ('DATSET1_NAME', ('DATASET1_TRAIN_FILE', USE_TRAIN), ('DATASET1_VAL_FILE', USE_VAL),  'DATASET1_TEST_FILE'),
    ('DATSET2_NAME', ('DATASET2_TRAIN_FILE', USE_TRAIN), ('DATASET2_VAL_FILE', USE_VAL),  'DATASET2_TEST_FILE'),
    ...
    ('DATSETN_NAME', ('DATASETN_TRAIN_FILE', USE_TRAIN), ('DATASETN_VAL_FILE', USE_VAL),  'DATASETN_TEST_FILE'),
]

'''

DATASETS_FOLDER = 'data/'
# DATASETS = [
#     ('Macmorpho', ('macmorpho-train.mm.txt', True), ('macmorpho-dev.mm.txt', True), 'macmorpho-test.mm.txt'),
#     ('Bosque', ('pt_bosque-ud-train.mm.txt', True), ('pt_bosque-ud-dev.mm.txt', True), 'pt_bosque-ud-test.mm.txt'),
#     ('GSD', ('pt_gsd-ud-train.mm.txt', True), ('pt_gsd-ud-dev.mm.txt', True), 'pt_gsd-ud-test.mm.txt'),
#     ('Linguateca', ('lgtc-train.mm.txt', True), ('lgtc-dev.mm.txt', True), 'lgtc-test.mm.txt')
# ]

DATASETS = [
    {'name': 'Macmorpho', 'trainFile': 'macmorpho-train.mm.txt', 'useTrain': True, 'valFile': 'macmorpho-dev.mm.txt',
        'useVal': True, 'testFile': 'macmorpho-test.mm.txt'},
    {'name': 'Bosque', 'trainFile': 'pt_bosque-ud-train.mm.txt', 'useTrain': True, 'valFile': 'pt_bosque-ud-dev.mm.txt',
        'useVal': True, 'testFile': 'pt_bosque-ud-test.mm.txt'},
    {'name': 'GSD', 'trainFile': 'pt_gsd-ud-train.mm.txt', 'useTrain': True, 'valFile': 'pt_gsd-ud-dev.mm.txt',
        'useVal': True, 'testFile': 'pt_gsd-ud-test.mm.txt'},
    {'name': 'Linguateca', 'trainFile': 'lgtc-train.mm.txt', 'useTrain': True, 'valFile': 'lgtc-dev.mm.txt',
        'useVal': True, 'testFile': 'lgtc-test.mm.txt'}
]

'''
================================================================================
============================= MODEL PARAMETERS =================================
================================================================================

'''

WORD_EMBEDDING_DIM = 350
CHAR_EMBEDDING_DIM = 70
BILSTM_SIZE = 150
MODEL_PATH = 'postag_sdict_WED_350_CED_70_BS_150.pt'


'''
================================================================================
============================= FILES PARAMETERS =================================
================================================================================



'''

EMBEDDINGS_PICKLE_PATH = {
    "embeddings1": "emd1.pickle",
    "embeddings2": "emd2.pickle",
    "embeddings3": "emd3.pickle",
    "embeddings4": "emd4.pickle",
}

TSNE_PICKLE_PATH = {
    "embeddings1": "tsne_emd1.pickle",
    "embeddings2": "tsne_emd2.pickle",
    "embeddings3": "tsne_emd3.pickle",
    "embeddings4": "tsne_emd4.pickle",
}

EMBEDDINGS_TXT_PATH = {
    "embeddings1": "emd1.txt",
    "embeddings2": "emd2.txt",
    "embeddings3": "emd3.txt",
    "embeddings4": "emd4.txt",
}

INFOS_PICKLE_PATH = "infos.pickle"
VOCAB_FILE = "vocab_file.txt"
INFO_FILE = "info_file.txt"

'''
================================================================================
============================== TSNE PARAMETERS =================================
================================================================================



'''
TRAIN_TSNE_EMBEDDINGS = {
    "embeddings1" : False,
    "embeddings2" : True,
    "embeddings3" : False,
    "embeddings4" : False,
}

'''
================================================================================
============================== PLOT PARAMETERS =================================
================================================================================



'''
PLOT_FLAG = {
    "embeddings1": True,
    "embeddings2" : False,
    "embeddings3" : False,
    "embeddings4" : False,
}


PLOT_COLORS = {
    "embeddings1": "yellow",
    "embeddings2" : "red",
    "embeddings3" : "blue",
    "embeddings4" : "green",
}

'''
================================================================================
========================== OUTPUT/LOG PARAMETERS ===============================
================================================================================

OUTPUT_PATH:        path to the output file with all the log from the program
LOG_LVL:            filter for the log that is going to be printed on the terminal.
                    if  LOG_LVL == 0: it will be printed erros, warnings, train and test output, tqdm
                        LOG_LVL == 1: it will be printed as in LOG_LVL=0 and success messages, descriptive log

STATE_DICT_PATH:    path for saving the model during training that is going to be
                    loaded for testing

'''

OUTPUT_PATH = 'output.txt'
LOG_LVL = 0
STATE_DICT_PATH = 'postag_sdict_WED_{}_CED_{}_BS_{}.pt'.format(WORD_EMBEDDING_DIM,
                                                                 CHAR_EMBEDDING_DIM,
                                                                 BILSTM_SIZE)
