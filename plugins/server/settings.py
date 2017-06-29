import storage.cv
import storage.fsinterface


LIEPIN_CVDB_PATH = 'output/liepin'
LIEPIN_FS = storage.fsinterface.FSInterface(LIEPIN_CVDB_PATH)
LIEPIN_STO_CV = storage.cv.CurriculumVitae(LIEPIN_FS)