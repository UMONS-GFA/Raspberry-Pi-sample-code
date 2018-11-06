import signal
import sys
import time
from Atlas_Sensors.smbus import AtlasSMBus
from gfa_logging import MsgLogger
from Atlas_Sensors.settings import MEASURE_INTERVAL, SENSOR_NUMBER, MSG_LOGGING_CONFIG, DATA_LOGGING_CONFIG

msg_logger = MsgLogger(name=MSG_LOGGING_CONFIG['name'], debug_mode=MSG_LOGGING_CONFIG['debug_mode'],
                       logging_to_console=MSG_LOGGING_CONFIG['logging_to_console'],
                       log_path=MSG_LOGGING_CONFIG['log_path'],
                       file_name=MSG_LOGGING_CONFIG['file_name'], max_bytes=MSG_LOGGING_CONFIG['max_bytes'],
                       backup_count=MSG_LOGGING_CONFIG['backup_count'], when=MSG_LOGGING_CONFIG['when'],
                       interval=MSG_LOGGING_CONFIG['interval'], header=MSG_LOGGING_CONFIG['header'],
                       date_formatter=MSG_LOGGING_CONFIG['date_formatter'])

data_logger = MsgLogger(name=DATA_LOGGING_CONFIG['name'], debug_mode=DATA_LOGGING_CONFIG['debug_mode'],
                        logging_to_console=DATA_LOGGING_CONFIG['logging_to_console'],
                        log_path=DATA_LOGGING_CONFIG['log_path'], file_name=DATA_LOGGING_CONFIG['file_name'],
                        max_bytes=DATA_LOGGING_CONFIG['max_bytes'], backup_count=DATA_LOGGING_CONFIG['backup_count'],
                        when=DATA_LOGGING_CONFIG['when'], interval=DATA_LOGGING_CONFIG['interval'],
                        header=DATA_LOGGING_CONFIG['header'], date_formatter=DATA_LOGGING_CONFIG['date_formatter'])


def handler(signum, frame):
    msg_logger.logger.info("Exiting {}".format(signum))
    sys.exit(signum)


def main():
    msg_logger.logger.info('_____ Started _____')
    msg_logger.logger.info('Saving in ' + DATA_LOGGING_CONFIG['log_path'])
    msg_logger.logger.info('Rotating data file each ' + str(DATA_LOGGING_CONFIG['when']))

    # Set the signal handler to terminate program properly
    signal.signal(signal.SIGTERM, handler)
    i2c_bus = AtlasSMBus()  # creates the I2C port object, specify the address or bus if necessary
    devices = i2c_bus.list_i2c_devices()

    while True:
        for i in range(len(devices)):
            i2c_bus.set_i2c_address(devices[i])
            try:
                info = str.split(i2c_bus.query("I"), ",")[1]
                sensor_id = str.lower(info) + SENSOR_NUMBER

                result = str(i2c_bus.query("R"))
                timestamp = str(int(time.time()))
                data_logger.logger.info("{0},{1},{2}".format(sensor_id, result, timestamp))

            except UnicodeDecodeError as e:
                msg_logger.logger.info("Problem with sensors reading {}".format(e))

        time.sleep(MEASURE_INTERVAL)


if __name__ == "__main__":
    main()
