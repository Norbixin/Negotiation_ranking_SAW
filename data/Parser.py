from model import Issue, Option
from typing import List
import xml.etree.ElementTree as et
import xml.dom.minidom as minidom


class Parser:
    @staticmethod
    def parse_file(path: str) -> List[Issue]:
        issues: List[Issue] = []
        tree: et = et.parse(path)
        root: et = tree.getroot()
        if root.tag != "Issues":
            return []
        for issue in root:
            if issue.tag == "Issue":
                issue_attribs = issue.attrib
                if "name" not in issue_attribs and "rating" not in issue_attribs:
                    continue
                _issue = Issue(issue.attrib["name"])
                _issue.rating = int(issue_attribs["rating"])
                for option in issue:
                    if option.tag == "Option":
                        option_attribs = option.attrib
                        if "name" not in option_attribs and "rating" not in option_attribs:
                            continue
                        _option = Option(option_attribs["name"])
                        _option.rating = int(option_attribs["rating"])
                        _issue.add_option(_option)
                issues.append(_issue)
        return issues

    @staticmethod
    def parse_issues(issues: List[Issue]) -> str:
        root = et.Element("Issues")
        for issue in issues:
            attrib = {"name": str(issue.name), "rating": str(issue.rating)}
            issue_node = et.SubElement(root, "Issue", attrib=attrib)
            for option in issue.options:
                attrib = {"name": str(option.name), "rating": str(option.rating)}
                option_node = et.SubElement(issue_node, "Option", attrib=attrib)
        return minidom.parseString(et.tostring(root, encoding='utf8')).toprettyxml(indent="\t")
