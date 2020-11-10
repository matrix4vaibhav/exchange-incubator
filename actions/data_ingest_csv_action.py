import yaml
from st2common.runners.base_action import Action
from mam.sdk import entitytype

__all__ = ["IngestCsvDataAction"]

class IngestCsvDataAction(Action):
    def __init__(self, config):
        super(IngestCsvDataAction, self).__init__(config)
        self._config = self.config
        self._credentials = self._config.get('credentials', None)
        self._data_file_path = self._config.get('data_file_path', None)
        self._action_type = self._config.get('action_type', None)
        self._entity_name = self._config.get('entity_name', None)
        
        if not self._config:
            raise ValueError('Missing config yaml')
        if not self._credentials:
            raise ValueError('Missing IBM Watson IoT credentials in config file')
        if not self._data_file_path:
            raise ValueError('Missing CSV data file path in config file')
        if not self._action_type:
            raise ValueError('Missing action type key in config file')
        if not self._entity_name:
            raise ValueError('Missing Entity name in config file')
            
    def run(self):
        if self._action_type == "LoadCsv":
            csv_data_path = self._data_file_path
        else:
            raise ValueError('Invalid Action Type !!') 
        success = False
        if csv_data_path:
            """----------Usage: 1. (X) Load Csv Data - using a CSV payload----------"""
            try:
                entitytype.load_metrics_data_from_csv(self._entity_name, csv_data_path, credentials=self._credentials)
                success = True
            except Exception as msg:
                print(f"FAILED STEP: {msg}\nFailed loading CSV data")
        return success
