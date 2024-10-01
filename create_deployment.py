from prefect import flow

SOURCE_REPO="https://github.com/GIRINATH25/prefect.git"

if __name__ == "__main__":
    flow.from_source(
        source=SOURCE_REPO,
        entrypoint="pro.py:repo_info", 
    ).deploy(
        name="my-first-deployment",
        work_pool_name="my-work-pool", # Work pool target
        cron="0 1 * * *", # Cron schedule (1am every day)
    )
