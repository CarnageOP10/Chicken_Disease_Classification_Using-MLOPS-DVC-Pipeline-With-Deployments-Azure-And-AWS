import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from Chicken_Disease_Classification.entitiy.config_entity import PrepareCallbacksConfig

class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    @property
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}",
        )
        # Ensure the TensorBoard log directory exists
        os.makedirs(tb_running_log_dir, exist_ok=True)
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    
    @property
    def _create_ckpt_callbacks(self):
        # Convert Path to string
        checkpoint_filepath = str(self.config.checkpoint_model_filepath)
        
        # Update file path to end with .keras
        if not checkpoint_filepath.endswith('.keras'):
            checkpoint_filepath = checkpoint_filepath.replace('.h5', '.keras')
        
        # Ensure the checkpoint directory exists
        checkpoint_dir = os.path.dirname(checkpoint_filepath)
        os.makedirs(checkpoint_dir, exist_ok=True)
        
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=checkpoint_filepath,
            save_best_only=True
        )

    def get_tb_ckpt_callbacks(self):
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]