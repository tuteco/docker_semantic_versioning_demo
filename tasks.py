from invoke import task

CONTAINER_NAME = 'hello_world'
IMAGE_NAME = f"tuteco/{CONTAINER_NAME}"
CONTAINER_INSTANCE = 'default'


@task
def build_local(context):
    """
        build an image from a Dockerfile with tag 'latest-dev'
    """
    context.run(f"docker build -t {IMAGE_NAME}:latest-dev . -f Dockerfile")


@task
def run_local(context):
    """
        run the local image with tag 'latest-dev'
    """
    context.run(f"docker run --rm --name {CONTAINER_NAME}-{CONTAINER_INSTANCE} {IMAGE_NAME}:latest-dev")


@task
def run(context):
    """
        run the image with tag 'latest'. pulled from docker hub
    """
    context.run(f"docker run --rm --name {CONTAINER_NAME}-{CONTAINER_INSTANCE} {IMAGE_NAME}:latest")