import pickle
from sklearn.preprocessing import LabelEncoder


class BodyPerformace:
    def __init__(self, params):
        self.params = params

    def encode_age(self):
        gender = pickle.load(open('encoders/Encode_Gender.sav', 'rb'))
        self.params["gender"] = str(int(gender.transform([self.params["gender"]])))

    def cluster_selection(self):
        self.encode_age()
        select_cluster = pickle.load(open('Models/clustering_KMean.sav', 'rb'))
        return select_cluster.predict([list(self.params.values())])

    def model_selection(self):
        cluster = self.cluster_selection()
        model = None
        if cluster == 0:
            model = pickle.load(open('Models/cluster0_XGBoost.sav', 'rb'))
        elif cluster == 1:
            model = pickle.load(open('Models/cluster1_SVC.sav', 'rb'))
        else:
            model = pickle.load(open('Models/cluster2_XGBoost.sav', 'rb'))
        return model

    def predict(self):
        model = self.model_selection()
        output_lbl = model.predict([self.params.values()])
        category = pickle.load(open('encoders/Encode_Category.sav', 'rb'))
        output_actual = category.inverse_transform(output_lbl)
        return output_actual
