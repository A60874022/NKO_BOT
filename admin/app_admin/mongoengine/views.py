from starlette_admin.contrib.mongoengine import ModelView
from .fields import DescriptionField
from .models import Topic


class TopicView(ModelView):

    model = Topic
    fields = [
        "id",
        "title",
        DescriptionField(
            "description",
            ),
        "image",
    ]
