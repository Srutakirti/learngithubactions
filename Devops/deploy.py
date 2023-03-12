import pathlib

# p = pathlib.Path(__file__)


# x = pathlib.Path("databricks_notebook_jobs\data_validations")

# print(x)

# for k in x.iterdir():
#     print(k)

def get_changed_jobs(diff_file):
    out = []
    with open(diff_file,"r") as f:
        all_files_paths = f.readlines()
        for file_path in all_files_paths:
            if file_path.split("/")[0] == "databricks_notebook_jobs":
                out.append(f'databricks_notebook_jobs/{file_path.split("/")[1]}')
    return set(out)


def get_jsons(folder_list):
    job_json_dict = {}
    for folder in folder_list:
        folder_path = pathlib.Path(folder)
        job_json_dict[folder] = list(folder_path.glob("*.json"))
    return job_json_dict

output = get_changed_jobs("diff.txt")

print(output)

output1 = get_jsons(output)

print(output1)


