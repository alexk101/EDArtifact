import pickle
import xgboost

model: xgboost.sklearn.XGBClassifier = pickle.load(open('SA_Detection.sav', 'rb'))
model.save_model('converted.bin')