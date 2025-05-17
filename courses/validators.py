from django.core.exceptions import ValidationError

def validate_video_file_extension(value):
    valid_extensions = ['.mp4', '.mov', '.avi']
    if not any(str(value).lower().endswith(ext) for ext in valid_extensions):
        raise ValidationError('Unsupported file extension.')
