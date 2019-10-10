""" fabfile template """
from fabric import task, Connection


def put_dir(con: Connection, from_dir: str, to_dir: str):
    """ put a directory to server.
    """
    con.local("tar cfz {0}.tar.gz {0}".format(from_dir))
    con.put("{}.tar.gz".format(from_dir), "{}".format(to_dir))
    con.run("tar zxf {1}/{0}.tar.gz -C {1}".format(from_dir, to_dir))
    con.local("rm {}.tar.gz".format(from_dir))


def mytask(con: Connection):
    con.local("echo 'do on local'")
    put_dir(con, "/tmp", "tmp")
    con.run("echo 'do something'")


@task(optional=[
    'log',
])
def sh(con, log=''):
    print(f"log: {log}")
    mytask(con)
