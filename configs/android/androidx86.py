import os

config = {
    "buildbot_json_path": "buildprops.json",
    "host_utils_url": "http://bm-remote.build.mozilla.org/tegra/tegra-host-utils.Linux.742597.zip",
    "robocop_package_name": "org.mozilla.roboexample.test",
    "device_ip": "127.0.0.1",
    "default_sut_port1": "20701",
    "default_sut_port2": "20700", # does not prompt for commands
    "tooltool_url": "http://tooltool.pvt.build.mozilla.org/build/sha512",
    "tooltool_cache_path": "/builds/slave/talos-slave/cached",
    "tooltool_cacheable_artifacts": {
        "avd_tar_ball": ("AVDs-x86-android-4.2_r1-build-2013-11-13-ubuntu.tar.gz",
            "3b2d18eb0194d82c70c5ee17487ccbac309f9b2e9839fe7ca4a27a9a06f6338bb24394476da78559685d99151fccc85fdde03297aa73ee2f7fb3183e11925c4d"),
    },
    ".avds_dir": "/home/cltbld/.android",
    "emulator_process_name": "emulator64-x86",
    "exes": {
        'adb': '/tools/android-sdk18/platform-tools/adb',
        'python': '/tools/buildbot/bin/python',
        'virtualenv': ['/tools/buildbot/bin/python', '/tools/misc-python/virtualenv.py'],
    },
    "env": {
        "DISPLAY": ":0.0",
        "PATH": "%(PATH)s:/tools/android-sdk18/tools:/tools/android-sdk18/platform-tools",
    },
    "default_actions": [
        'clobber',
        'read-buildbot-config',
        'download-cacheable-artifacts',
        'setup-avds',
        'start-emulators',
        'download-and-extract',
        'create-virtualenv',
        'install',
        'run-tests',
        'stop-emulators',
    ],
    "emulators": [
        {
            "name": "test-1",
            "device_id": "emulator-5554",
            "http_port": "8854", # starting http port to use for the mochitest server
            "ssl_port": "4454", # starting ssl port to use for the server
            "emulator_port": 5554,
            "sut_port1": 20701,
            "sut_port2": 20700
        },
        {
            "name": "test-2",
            "device_id": "emulator-5556",
            "http_port": "8856", # starting http port to use for the mochitest server
            "ssl_port": "4456", # starting ssl port to use for the server
            "emulator_port": 5556,
            "sut_port1": 20703,
            "sut_port2": 20702
        },
        {
            "name": "test-3",
            "device_id": "emulator-5558",
            "http_port": "8858", # starting http port to use for the mochitest server
            "ssl_port": "4458", # starting ssl port to use for the server
            "emulator_port": 5558,
            "sut_port1": 20705,
            "sut_port2": 20704
        },
        {
            "name": "test-4",
            "device_id": "emulator-5560",
            "http_port": "8860", # starting http port to use for the mochitest server
            "ssl_port": "4460", # starting ssl port to use for the server
            "emulator_port": 5560,
            "sut_port1": 20707,
            "sut_port2": 20706
        }
    ],
    "test_suite_definitions": {
        "jsreftest": {
            "category": "reftest",
            "extra_args": ["../jsreftest/tests/jstests.list",
                "--extra-profile-file=jsreftest/tests/user.js"]
        },
        "mochitest-1": {
            "category": "mochitest",
            "extra_args": ["--total-chunks", "2", "--this-chunk", "1", "--run-only-tests", "androidx86.json"],
        },
        "mochitest-2": {
            "category": "mochitest",
            "extra_args": ["--total-chunks", "2", "--this-chunk", "2", "--run-only-tests", "androidx86.json"],
        },
        "mochitest-gl": {
            "category": "mochitest",
            "extra_args": ["--test-manifest", "gl.json"],
        },
        "reftest-1": {
            "category": "reftest",
            "extra_args": ["--total-chunks", "3", "--this-chunk", "1",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-2": {
            "category": "reftest",
            "extra_args": ["--total-chunks", "3", "--this-chunk", "2",
                "tests/layout/reftests/reftest.list"]
        },
        "reftest-3": {
            "category": "reftest",
            "extra_args": ["--total-chunks", "3", "--this-chunk", "3",
                "tests/layout/reftests/reftest.list"]
        },
        "crashtest": {
            "category": "reftest",
            "extra_args": ["tests/testing/crashtest/crashtests.list"]
        },
        "xpcshell": {
            "category": "xpcshell",
            "extra_args": ["--manifest", "tests/xpcshell_android.ini"]
        },
        "robocop-1": {
            "category": "mochitest",
            "extra_args": ["--total-chunks", "3", "--this-chunk", "1", "--robocop-path=../..",
                "--robocop-ids=fennec_ids.txt", "--robocop=robocop.ini"],
        },
        "robocop-2": {
            "category": "mochitest",
            "extra_args": ["--total-chunks", "3", "--this-chunk", "2", "--robocop-path=../..",
                "--robocop-ids=fennec_ids.txt", "--robocop=robocop.ini"],
        },
        "robocop-3": {
            "category": "mochitest",
            "extra_args": ["--total-chunks", "3", "--this-chunk", "3", "--robocop-path=../..",
                "--robocop-ids=fennec_ids.txt", "--robocop=robocop.ini"],
        },
    }, # end of "test_definitions"
    # test harness options are located in the gecko tree
    "in_tree_config": "config/mozharness/android_x86_config.py",
    "download_minidump_stackwalk": True,
    "default_blob_upload_servers": [
         "https://blobupload.elasticbeanstalk.com",
    ],
    "blob_uploader_auth_file" : os.path.join(os.getcwd(), "oauth.txt"),
}
