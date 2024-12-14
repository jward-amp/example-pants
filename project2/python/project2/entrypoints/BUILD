pex_binary(
    name="bin",
    dependencies=[
        "project2/python/project2/entrypoints/fizzbuzz",
        "project2/python/project2/entrypoints/whichpanda",
    ],
    layout="packed",
    environment="docker_linux",
)

docker_image(
    name="project2",
    image_tags=["local"],
    build_platform=["linux/amd64"],
)
