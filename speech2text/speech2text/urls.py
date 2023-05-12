"""
URL configuration for speech2text project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from core.schemas import ChatGPTSchema
from django.contrib import admin
from django.urls import path
from ninja_extra import NinjaExtraAPI, api_controller, route

# from core.huggingface_services import speech2text_serivce
from core.services import (
    speech2text_serivce,
    chatgpt_service,
    elevenlabs_service,
)
from ninja import File
from ninja.files import UploadedFile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

api = NinjaExtraAPI()


@api_controller("/whisper")
class SpeechController:
    @route.post(
        "/send",
        tags=["whisper"],
    )
    def speech_endpoint(request, file: UploadedFile = File(...)):
        """
        Create transcription from audio file
        """
        # Always convert file to saved file
        path = default_storage.save(file.name, ContentFile(file.read()))
        output = {"transcript": speech2text_serivce(us_file=path, uploaded_file=file)}
        default_storage.delete(path)
        return output


@api_controller("/chatgpt")
class ChatGPTController:
    @route.post(
        "/send",
        tags=["chatgpt"],
    )
    def chatgpt_endpoint(self, request, text: str):
        """
        Ask a funny question to chatgpt
        """
        # Always convert file to saved file
        return chatgpt_service(text)


@api_controller("/elevenlabs")
class ElevenLabsController:
    @route.post(
        "/send",
        tags=["elevenlabs"],
    )
    def elevenlabs_endpoint(self, request, text: str):
        """
        Text to speech using elevenlabs
        """
        # Always convert file to saved file
        return elevenlabs_service(text)


api.register_controllers(ChatGPTController)
api.register_controllers(SpeechController)
api.register_controllers(ElevenLabsController)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", api.urls),
]
