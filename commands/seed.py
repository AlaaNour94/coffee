import logging
from baseapp import app
from database.models import CoffeePod, CoffeeMachine

logger = logging.getLogger(__name__)


def read_data(path):
    res = []
    with open(path, 'r') as machines_data:
        lines = machines_data.readlines()
        for machine_data in lines:
            res.append([x.strip() for x in machine_data.split('–')])

    return res


@app.cli.command("seed_machines_data")
def seed_machines_data():
    """ Seed Machine data into Database """
    logger.info("Seeding Machines data into database")

    machines = []

    for machine_data in read_data('commands/machines_data.txt'):

        machines.append(CoffeeMachine(
            name=machine_data[0].upper(),
            type=machine_data[1].upper(),
            model=machine_data[2].upper(),
            water_line=True if machine_data[3].upper() == "TRUE" else False,
        ))
    try:
        CoffeeMachine.objects.insert(machines)
    except Exception as e:
        logger.error(f"Error {e} while seeding machines")


@app.cli.command("seed_pods_data")
def seed_pods_data():
    """ Seed Pods data into Database """

    logger.info("Seeding Pods data into database")

    pods = []

    for pod_data in read_data('commands/pods_data.txt'):

        pods.append(CoffeePod(
            name=pod_data[0].upper(),
            type=pod_data[1].upper(),
            size=int(pod_data[2]),
            flavor=pod_data[3].upper(),
        ))

    try:
        CoffeePod.objects.insert(pods)
    except Exception as e:
        logger.error(f"Error {e} while seeding pods")


app.cli.add_command(seed_machines_data)
app.cli.add_command(seed_pods_data)
