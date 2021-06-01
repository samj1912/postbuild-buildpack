import subprocess

import libcnb


def detector(context: libcnb.DetectContext) -> libcnb.DetectResult:
    return libcnb.DetectResult(passed=(context.application_dir / "postBuild").exists())


def builder(context: libcnb.BuildContext) -> libcnb.BuildResult:
    print("Running postBuild Buildpack", flush=True)
    (context.application_dir / "postBuild").chmod(0o755)
    print("Executing postBuild script", flush=True)
    subprocess.run("./postBuild", cwd=context.application_dir, check=True)
    return libcnb.BuildResult()


if __name__ == "__main__":
    libcnb.run(detector=detector, builder=builder)
