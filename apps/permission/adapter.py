from casbin import persist


class DjangoAdapter(persist.Adapter):
    """the interface for Casbin adapters."""

    def __init__(self, m):
        self.adapter_models = m

    def load_policy(self, model):
        """loads all policy rules from the storage."""
        # for db in self.adapter_models:
        #     for qs in db.objects.all():
        #         for item in qs.adapter():
        #             values = list(item.values())
        #             # print(values)
        #             persist.load_policy_line(', '.join(values), model)
        for line in self.adapter_models.objects.all():
            persist.load_policy_line(str(line), model)

    def save_policy(self, model):
        """saves all policy rules to the storage."""
        pass

    def add_policy(self, sec, ptype, rule):
        """adds a policy rule to the storage."""
        pass

    def remove_policy(self, sec, ptype, rule):
        """removes a policy rule from the storage."""
        pass

    def remove_filtered_policy(self, sec, ptype, field_index, *field_values):
        """removes policy rules that match the filter from the storage.
        This is part of the Auto-Save feature.
        """
        pass