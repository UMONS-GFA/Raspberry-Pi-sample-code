MEASURE_INTERVAL = 60
SENSOR_NUMBER = "001"

# Used to debug
MSG_LOGGING_CONFIG = {
    'name': 'msg_logger',
    'debug_mode': False,
    'logging_to_console': False,
    'log_path': 'logs',
    'file_name': 'msg_log',
    'max_bytes': 262144,
    'backup_count': 30,
    'when': 'D',
    'interval': 1,
    'header': '',
    'date_formatter': True
}

# Used to records sensors data
DATA_LOGGING_CONFIG = {
    'name': 'data_logger',  # used by the script to distinguish the logger
    'debug_mode': False,
    'logging_to_console': False,
    'log_path': 'data',
    'file_name': 'data_log',
    'max_bytes': 1048576,
    'backup_count': 30,
    'when': 'H',      # Settings period to minute overwrite data_log rotating file !!
    'interval': 1,
    'header': '',
    'date_formatter': False

}
