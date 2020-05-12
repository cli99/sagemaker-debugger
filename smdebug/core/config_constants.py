CLAIM_FILENAME = "claim.smd"
CONFIG_FILE_PATH_ENV_STR = "SMDEBUG_CONFIG_FILE_PATH"
DEFAULT_WORKER_NAME = "worker_0"
DEFAULT_CONFIG_FILE_PATH = "/opt/ml/input/config/debughookconfig.json"
EXPORT_TENSORBOARD_KEY = "export_tensorboard"
TENSORBOARD_DIR_KEY = "tensorboard_dir"
CONFIG_REDUCTION_CONFIGS_KEY = "reduction_configs"
CONFIG_SAVE_CONFIGS_KEY = "save_configs"
CONFIG_OUTDIR_KEY = "LocalPath"
CONFIG_HOOK_PARAMS_KEY = "HookParameters"
CONFIG_COLLECTION_CONFIG_KEY = "CollectionConfigurations"
CONFIG_COLLECTION_NAME_KEY = "CollectionName"
CONFIG_COLLECTION_PARAMS_KEY = "CollectionParameters"
CONFIG_DRYRUN_KEY = "dry_run"
CONFIG_RDN_CFG_KEY = "reduction_config"
CONFIG_INCLUDE_REGEX_KEY = "include_regex"
CONFIG_INCLUDE_WORKERS_KEY = "include_workers"
CONFIG_SAVE_ALL_KEY = "save_all"
TENSORBOARD_CONFIG_FILE_PATH_ENV_STR = "TENSORBOARD_CONFIG_FILE_PATH"
SM_PROFILER_FILE_PATH_ENV_STR = "SM_PROFILER_FILE_PATH"
DEFAULT_SAGEMAKER_METRICS_PATH = "SAGEMAKER_METRICS_DIRECTORY"
DEFAULT_SAGEMAKER_OUTDIR = "/opt/ml/output/tensors"
DEFAULT_SAGEMAKER_TENSORBOARD_PATH = "/opt/ml/input/config/tensorboardoutputconfig.json"
DEFAULT_SAGEMAKER_PROFILER_PATH = "/opt/ml/input/config/profilerconfig.json"
DEFAULT_COLLECTIONS_FILE_NAME = "worker_0_collections.json"
CHECKPOINT_CONFIG_FILE_PATH_ENV_VAR = "CHECKPOINT_CONFIG_FILE_PATH"
CHECKPOINT_DIR_KEY = "LocalPath"
DEFAULT_CHECKPOINT_CONFIG_FILE = "/opt/ml/input/config/checkpointconfig.json"
METADATA_FILENAME = "metadata.json"
LATEST_GLOBAL_STEP_SEEN = "latest-global-step-seen"
LATEST_GLOBAL_STEP_SAVED = "latest-global-step-saved"
LATEST_MODE_STEP = "latest-mode-step"
TRAINING_RUN = "training-run"

INCOMPLETE_STEP_WAIT_WINDOW_KEY = "SMDEBUG_INCOMPLETE_STEP_WAIT_WINDOW"
INCOMPLETE_STEP_WAIT_WINDOW_DEFAULT = 1000

MISSING_EVENT_FILE_RETRY_LIMIT_KEY = "SMDEBUG_MISSING_EVENT_FILE_RETRY_LIMIT"
MISSING_EVENT_FILE_RETRY_LIMIT = 100

TRAINING_END_DELAY_REFRESH_KEY = "SMDEBUG_TRAINING_END_DELAY_REFRESH"
TRAINING_END_DELAY_REFRESH_DEFAULT = 1

CALLABLE_CACHE_ENV_VAR = "SMDEBUG_KERAS_CALLABLE_CACHE_TYPE"
DEFAULT_CALLABLE_CACHE = "CACHE_PER_MODE"
