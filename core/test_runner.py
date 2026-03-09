import subprocess


class SentinelRunner:

    def run_tests(self, workers=1, browser=None, network="normal", failure="none"):

        cmd = ["pytest"]

        # parallel workers
        if workers and workers > 1:
            cmd.extend(["-n", str(workers)])

        # browser selection
        if browser:
            cmd.extend(["-k", browser])

        # network chaos
        if network:
            cmd.extend(["--network", network])

        # failure injection
        if failure:
            cmd.extend(["--failure", failure])

        print("Running command:", " ".join(cmd))

        subprocess.run(cmd)