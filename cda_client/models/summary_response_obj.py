from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.summary_response_obj_result_item_type_0 import SummaryResponseObjResultItemType0


T = TypeVar("T", bound="SummaryResponseObj")


@_attrs_define
class SummaryResponseObj:
    """
    Attributes:
        result (list[None | SummaryResponseObjResultItemType0]): List of query result json objects
        query_sql (None | str): SQL Query generated to yield the results
    """

    result: list[None | SummaryResponseObjResultItemType0]
    query_sql: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.summary_response_obj_result_item_type_0 import SummaryResponseObjResultItemType0

        result = []
        for result_item_data in self.result:
            result_item: dict[str, Any] | None
            if isinstance(result_item_data, SummaryResponseObjResultItemType0):
                result_item = result_item_data.to_dict()
            else:
                result_item = result_item_data
            result.append(result_item)

        query_sql: None | str
        query_sql = self.query_sql

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "result": result,
                "query_sql": query_sql,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.summary_response_obj_result_item_type_0 import SummaryResponseObjResultItemType0

        d = dict(src_dict)
        result = []
        _result = d.pop("result")
        for result_item_data in _result:

            def _parse_result_item(data: object) -> None | SummaryResponseObjResultItemType0:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    result_item_type_0 = SummaryResponseObjResultItemType0.from_dict(data)

                    return result_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(None | SummaryResponseObjResultItemType0, data)

            result_item = _parse_result_item(result_item_data)

            result.append(result_item)

        def _parse_query_sql(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        query_sql = _parse_query_sql(d.pop("query_sql"))

        summary_response_obj = cls(
            result=result,
            query_sql=query_sql,
        )

        summary_response_obj.additional_properties = d
        return summary_response_obj

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
