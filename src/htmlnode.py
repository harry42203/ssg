class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props != None: 
            ret_str = ""
            for item in self.props:
                ret_str += f' {item}="{self.props[item]}"'
            return ret_str
        
    def __repr__(self):
        return f"HTMLNode Tag:{self.tag} Value:{self.value} Children:{self.children} Props:{self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.value == None or len(self.value) == 0:
            raise ValueError
        if self.tag == None or len(self.tag) == 0:
            return f"{self.value}"
        if self.tag == "pre_code":
            f"<pre><{self.tag}>{self.value}</{self.tag}></pre>"
        if self.props != None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not isinstance(children, list) or len(children) == 0:
            raise ValueError("Non-empty list of children required")
        super().__init__(tag, "", children, props)

    def to_html(self):
        if self.tag == None or len(self.tag) == 0:
            raise ValueError("tag required")
        if self.children == None:
            raise ValueError("children required")
        temp_str = ""
        for child in self.children:
            temp_str += child.to_html()
        return f"<{self.tag}>{temp_str}</{self.tag}>"
        