pex_binary(
    name="bin",
    dependencies=[
        "project2/python/entrypoints/fizzbuzz",
    ],
    layout="packed",
    environment="docker_linux",
)

docker_image(
    name="project2",
    image_tags=["local"],
)
