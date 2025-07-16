from langchain.tools import StructuredTool
from pydantic.v1 import BaseModel

def write_report(filename, html):
    with open(filename, 'w') as f:
        f.write(html)

class WriteReportArgsSchema(BaseModel):
    filename: str
    html: str

#receber um HTML do chatGPT e criar um arquivo HTML no disco
write_report_tool = StructuredTool.from_function(
    name="write_report",
    description="Writes an HTML file to disk. Use this tool whenever you want to save a report.",
    func=write_report,
    args_schema=WriteReportArgsSchema,
)