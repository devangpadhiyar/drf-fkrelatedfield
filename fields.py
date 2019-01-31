import json

from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_text
from django.utils.translation import ugettext_lazy as _
from rest_framework.relations import RelatedField
from rest_framework.renderers import JSONRenderer


class FKRelatedField(RelatedField):
    """
    This field is for representation of fk fields as dictionary
    i.e
    use this in serializer as below
    fk_field = FkRelatedField(fk=None, queryset=Queryset.objects.all(), serializer=SerializerClass)

    this allow fk_field accept pk value as input and gives dictionary representation of serializer as output
    """
    default_error_messages = {
        'does_not_exist': _('Object with {unique_field}={value} does not exist.'),
        'invalid': _('Invalid value.'),
    }

    def __init__(self, fk=None, serializer=None, **kwargs):
        assert fk is not None, 'The `unique_field` argument is required.'
        self.unique_field = fk
        self.serializer = serializer
        super(FKRelatedField, self).__init__(**kwargs)

    def to_internal_value(self, data):
        try:
            return self.get_queryset().get(**{self.unique_field: data})
        except ObjectDoesNotExist:
            self.fail('does_not_exist', unique_field=self.unique_field, value=smart_text(data))
        except (TypeError, ValueError):
            self.fail('invalid')

    def to_representation(self, obj):
        return json.loads(JSONRenderer().render(data=self.serializer(obj).data).decode())
