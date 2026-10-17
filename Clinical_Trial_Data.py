import requests

url = "https://clinicaltrials.gov/api/v2/studies"
params = {
   "query.cond": "obesity",     # swap in anything: "lung cancer", "alzheimer", "ALS", etc. 
    "filter.overallStatus": "RECRUITING",
    "sort": "LastUpdatePostDate:desc",
    "pageSize": 1,
    "fields": "BriefTitle|BriefSummary|Condition|ArmsInterventionsModule|OverallStatus|StudyFirstPostDate|LastUpdatePostDate|StartDate",
}

data = requests.get(url, params=params, timeout=30).json()
p = data["studies"][0]["protocolSection"]

title         = p["identificationModule"]["briefTitle"]
overview      = p.get("descriptionModule", {}).get("briefSummary", "")
conditions    = p.get("conditionsModule", {}).get("conditions", [])
interventions = p.get("armsInterventionsModule", {}).get("interventions", [])
status        = p.get("statusModule", {}).get("overallStatus", "")

print(list(p.keys()))
print("Title:     ", title)
print("Status:    ", status)
print("Conditions:", ", ".join(conditions))
print("Overview:  ", overview)
print("Treatments:")
for item in interventions:
    print(f"  - {item.get('name')} ({item.get('type')})")


status_mod  = p.get("statusModule", {})
first_posted = status_mod.get("studyFirstPostDateStruct", {}).get("date", "")
last_update  = status_mod.get("lastUpdatePostDateStruct", {}).get("date", "")
start_date   = status_mod.get("startDateStruct", {}).get("date", "")

print("First posted:", first_posted)
print("Last update: ", last_update)
print("Start date:  ", start_date)