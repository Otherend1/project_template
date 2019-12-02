import os
cur_dir = os.path.dirname(os.path.realpath(__file__))

settings = {
   "dumps": {
       "iris_svm_model_path" : os.path.join(cur_dir, "model/weights/iris_svm_model.joblib"),
   }
}
