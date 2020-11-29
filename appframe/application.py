from pathlib import Path
from eprint import eprint
from eprint.str import info
import importlib
from . import singleton
from .log import verbose


class Application:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.feature_map = {}

    def _load_features(self):
        features_dir = Path(singleton.app_dir, "features").resolve()

        for file_path in Path(features_dir).glob("*.py"):
            feature_name = file_path.stem
            verbose(1, info("Loading feature from {}", file_path))
            #  feature_module = import_module()
            spec = importlib.util.spec_from_file_location(
                f"webplane.app_features.{feature_name}", file_path
            )
            feature_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(feature_module)
            self.feature_map[feature_name] = feature_module

    def _sort_features(self):
        # If there is an AFTER_FEATURE attribute, make sure that
        # feature will be activated first
        sorted_list = []
        for feature_name, feature_module in self.feature_map.items():
            after_feature = getattr(feature_module, "AFTER_FEATURE", None)
            if after_feature and after_feature not in sorted_list:
                sorted_list.insert(0, after_feature)
            if feature_name not in sorted_list:
                sorted_list.append(feature_name)
        new_feature_map = {}
        for feature_name in sorted_list:
            new_feature_map[feature_name] = self.feature_map[feature_name]
        self.feature_map = new_feature_map

    def _activate_features(self):
        for feature_module in self.feature_map.values():
            feature_module.activate(*self.args, **self.kwargs)

    def run(self):
        eprint.info("Starting application from {}", singleton.app_dir)
        self._load_features()
        self._sort_features()
        self._activate_features()
