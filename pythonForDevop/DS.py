#for i in range(10):
 #   print(i)





listofcloud = ["azure","aws","gcp","oracle","ibm"]
listofenv = ["dev","test","QA","PROD"]

    #list iteration

for cloud in listofcloud:
    if cloud == "azure":
        print("Azure is emerging")

        #dictionary

        dict_of_cloud = {
            "AWS":"Amazon web service",
            "GCP":"Google cloud platform",
            "Azure":"MS cloud"
        }

        print(dict_of_cloud["AWS"])

        dict_of_cloud.update ("cloudmera": "cloudtera")