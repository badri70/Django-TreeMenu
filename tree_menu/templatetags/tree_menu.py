from django import template
from django.urls import resolve
from tree_menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path

    items = list(
        MenuItem.objects.filter(menu_name=menu_name).select_related('parent')
    )

    item_dict = {item.id: item for item in items}

    # строим дерево
    tree = {}
    for item in items:
        parent_id = item.parent_id
        if parent_id:
            tree.setdefault(parent_id, []).append(item)
        else:
            tree.setdefault(None, []).append(item)

    active_item = None
    for item in items:
        if item.get_url() == current_url:
            active_item = item
            break

    expanded_ids = set()
    if active_item:
        node = active_item
        while node:
            expanded_ids.add(node.id)
            node = node.parent

    return {
        "tree": tree,
        "root_items": tree.get(None, []),
        "expanded_ids": expanded_ids,
        "active_id": active_item.id if active_item else None,
    }

@register.filter
def get_item(dict_obj, key):
    return dict_obj.get(key)