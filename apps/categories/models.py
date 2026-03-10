from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="children"
    )
    image = models.ImageField(
        upload_to="categories/",
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
        unique_together = ('name', 'parent')

    def clean(self):
        if self.pk and self.parent_id == self.pk:
            raise ValidationError('Category cannot be its own parent!')
        if self.parent and self.parent.parent is not None:
            raise ValidationError('Child category cannot be a parent!')

    def save(self, *args, **kwargs):
        self.full_clean()
        if self.parent is None:
            self.image = None
        super().save(*args, **kwargs)

    @property
    def is_root(self):
        return self.parent is None

    @property
    def is_leaf(self):
        return not self.children.exists()

    def __str__(self):
        return self.name