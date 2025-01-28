import argparse
from datetime import datetime

import asana
from asana.rest import ApiException

def get_incompleted_tasks(api, section_gid, opts):
    tasks = api.get_tasks_for_section(section_gid, opts)
    substaks = []
    
    for task in tasks:
        if not task["completed"]:
            print(task["name"])

            substaks = api.get_subtasks_for_task(task["gid"], opts)

            for subtask in substaks:
                print("    - " + subtask["name"])
            print()

def get_last_completed_tasks(api, section_gid, opts):
    tasks = api.get_tasks_for_section(section_gid, opts)
    substaks = []
    
    for task in tasks:
        if task["completed"]:
            print("-" + task["name"])

            # task_date = datetime_object = datetime.strptime(task["modified_at"], '%Y-%m-%d %H:%M:%S.%F')

            substaks = api.get_subtasks_for_task(task["gid"], opts)

            for subtask in substaks:
                print("    -" + subtask["name"])
            print()

def get_config():
    # Configure arguments
    parser = argparse.ArgumentParser(description="Asana tasks list", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-a", "--all", action="store_true", help="Show incompleted")
    args = vars(parser.parse_args())

    # Configure personal access token
    configuration = asana.Configuration()
    configuration.access_token = '2/1201954301289528/1206807859685071:36fe2574f3c2448adea90608e74f9d76'
    api_client = asana.ApiClient(configuration)

    return args, api_client

def main():
    args, api_client = get_config()

    # Construct resource API Instance
    users_api_instance = asana.UsersApi(api_client)
    tasks_api_instance = asana.TasksApi(api_client)

    user_gid = "me"
    section_gid = "1203045151803012"

    opts = {}
    task_opts = {
        "opt_fields": "name,completed,completed_at,modified_at"
    }

    try:
        # Get your user info
        me = users_api_instance.get_user(user_gid, opts)

        if args['all']:
            task_opts.update({"limit": 5})
            get_last_completed_tasks(tasks_api_instance, section_gid, task_opts)
        else:
            get_incompleted_tasks(tasks_api_instance, section_gid, task_opts)

    except ApiException as e:
        print("Exception when calling Asana API: %s\n" % e)

if __name__ == '__main__':
    main()