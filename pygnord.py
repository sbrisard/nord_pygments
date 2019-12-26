"""Nord highlighting style for Pygments

Nord is an arctic, north-bluish color palette by Arctic Ice Studio
<development@arcticicestudio.com> (https://www.arcticicestudio.com)

License: BSD-3 Clause License. See LICENSE for details
"""

from pygments.style import Style
from pygments.token import (
    Keyword,
    Name,
    Comment,
    String,
    Error,
    Number,
    Operator,
    Punctuation,
    Generic,
    Whitespace,
)

nord0 = "#2e3440"
nord1 = "#3b4252"
nord2 = "#434c5e"
nord3 = "#4c566a"
nord3_bright = "#616e87"

nord4 = "#d8dee9"
nord5 = "#e5e9f0"
nord6 = "#eceff4"

nord7 = "#8fbcbb"
nord8 = "#88c0d0"
nord9 = "#81a1c1"
nord10 = "#5e81ac"

nord11 = "#bf616a"
nord12 = "#d08770"
nord13 = "#ebcb8b"
nord14 = "#a3be8c"
nord15 = "#b48ead"


class NordStyle(Style):
    background_color = nord0
    default = nord4

    styles = {
        Whitespace: nord4,
        Comment: f"italic {nord3_bright}",
        Comment.Preproc: nord10,
        Keyword: f"bold {nord9}",
        Keyword.Pseudo: f"nobold {nord9}",
        Keyword.Type: f"nobold {nord9}",
        Operator: nord9,
        Operator.Word: f"bold {nord9}",
        Name: nord4,
        Name.Builtin: nord9,
        Name.Function: nord8,
        Name.Class: nord7,
        Name.Namespace: nord7,
        Name.Exception: nord11,
        Name.Variable: nord4,
        Name.Constant: nord7,
        Name.Label: nord7,
        Name.Entity: nord12,
        Name.Attribute: nord7,
        Name.Tag: nord9,
        Name.Decorator: nord12,
        Punctuation: nord6,
        String: nord14,
        String.Doc: nord3_bright,
        String.Interpol: nord14,
        String.Escape: nord13,
        String.Regex: nord13,
        String.Symbol: nord14,
        String.Other: nord14,
        Number: nord15,
        Generic.Heading: f"bold {nord8}",
        Generic.Subheading: f"bold {nord8}",
        Generic.Deleted: nord11,
        Generic.Inserted: nord14,
        Generic.Error: nord11,
        Generic.Emph: "italic",
        Generic.Strong: "bold",
        Generic.Prompt: f"bold {nord3}",
        Generic.Output: nord4,
        Generic.Traceback: nord11,
        Error: nord11,
    }
