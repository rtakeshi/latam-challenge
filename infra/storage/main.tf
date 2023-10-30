module "provider_module"{
    source = "../modules/provider"
}


resource "google_storage_bucket" "latam_challenge_bucket"{
 
  project = "terraform-gcp-402419"
  name = "latam-challenge-rtkseo-bucket"
  location = "US"



  labels = {
    "env" = "prod"
  }

  


 
  
}

