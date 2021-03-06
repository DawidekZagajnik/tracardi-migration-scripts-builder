from pydantic import BaseModel
from app.domain.mappings_difference import MappingsDifference
from app.service.rules_engine import RulesEngine
from app.domain.index_migration_schema import IndexMigrationSchema


class IndexDifference(BaseModel):
    """
    Represents difference between old and new index mappings:
        from_index, to_index="index-name",
        multi="<multi-index-or-not>",
        difference=MappingsDifference(added=[...], removed=[...], changed=[...])
    """
    from_index: str
    to_index: str
    multi: bool
    difference: MappingsDifference

    def to_migration(self):
        ops, custom_worker_required = RulesEngine(difference=self.difference).get_operations()
        return IndexMigrationSchema(
            from_index=self.from_index,
            to_index=self.to_index,
            multi=self.multi,
            operations=ops,
            custom_worker_required=custom_worker_required
        )
