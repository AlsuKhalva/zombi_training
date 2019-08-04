from model.hw_group import Group
import random

def test_edit_some_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="VVVVVVV"))
    old_groups = db.get_group_list()
    index = random.choice(range(len(old_groups)))
    id = old_groups[index].id
    group = Group(name="111", id=id)
    app.group.edit_group_by_id(id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.rstrip())
        assert sorted(list(map(clean, new_groups)), key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                                  key=Group.id_or_max)

#def test_edit_first_group_name(app):
 #   if app.group.count() == 0:
  #      app.group.create(Group(name="VVVVVVV"))
  #  old_groups = app.group.get_group_list()
  #  group = Group(name="ZUMZUM")
  #  group.id = old_groups[0].id
  #  app.group.edit_first_group(group)
  #  new_groups = app.group.get_group_list()
  #  assert len(old_groups) == len(new_groups)
  #  old_groups[0] = group
  #  assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_first_group_header(app):
 #   old_groups = app.group.get_group_list()
  #  app.group.edit_first_group(Group(header="Bebbb"))
   # new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
