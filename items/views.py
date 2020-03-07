from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import template

from items.forms import ItemForm
from items.models import Item



class ItemListView(ListView):
    """ Renders a list of all items. """
    model = Item

    def get(self, request):
        """ GET a list of items. """
        user_items = None
        if self.request.user.is_authenticated:
          user_items = Item.objects.filter(author=request.user)
        all_items= Item.objects.filter(is_public=True)

        return render(request, 'list.html', {
          'user_items': user_items,
          'all_items': all_items
        })

class ItemDetailView(DetailView):
    """ Renders a specific item based on it's slug."""
    model = Item

    def get(self, request, slug):
        """ Returns a specific item by slug. """
        item = get_object_or_404(Item, slug=slug)
        return render(request, 'item.html', {
          'item': item
        })

class ItemNew(CreateView):
    model = Item

    def get(self, request):
      """ Prints the form """
      item_form = ItemForm()
      return render(request, 'add_item.html', {
        'item_form': item_form
      })

    def post(self, request):
      """processes the form and adds a blog """
      form = ItemForm(request.POST)
      form.instance.author = self.request.user
      print(form)
      if form.is_valid():
        item = form.save()
        return HttpResponseRedirect(reverse('items-details-page', args=[item.slug] ))
      else:
        return render(request, 'add_item.html', {
        'item_form': form,
      })


class ItemUpdate(UpdateView):
    model= Item
    fields = ['food_name', 'description', 'is_public']
    template_name_suffix = '_update_form'

    def post(self, request, slug):
      """processes the form and adds a blog """
      obj = get_object_or_404(Item, slug=slug)
      form = ItemForm(request.POST, instance=obj)
      if form.is_valid():
        form.save()
        print(form)
        return HttpResponseRedirect(reverse('pantry-details-page', args=[slug] ))
      else:
        return render(request, 'items/item_update_form.html', {
          'form': form,
        })

def delete_object(request, slug):
  Item.objects.filter(slug=slug).delete()
  return HttpResponseRedirect(reverse('pantry-list-page'))