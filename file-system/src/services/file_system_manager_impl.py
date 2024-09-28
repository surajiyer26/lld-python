from models.folder import Folder
from models.file import File
from models.file_system_item import FileSystemItem
from typing import Optional, List

class FileSystemManagerImpl:
    def __init__(self, root_name: str):
        self.file_system = Folder(root_name)

    def add_file_or_folder(self, parent_folder_name: str, name: str, is_folder: bool) -> bool:
        parent_folder = self._find_folder(parent_folder_name, self.file_system)
        if parent_folder:
            if parent_folder.get_item(name) is None:  
                if is_folder:
                    parent_folder.add_item(Folder(name))
                else:
                    parent_folder.add_item(File(name))
                return True
        return False

    def move_file_or_folder(self, source_name: str, destination_folder: str) -> bool:
        source_item = self._find_item(source_name, self.file_system)  
        destination = self._find_folder(destination_folder, self.file_system)

        if source_item and destination:
            current_parent = self._find_parent(source_item)
            if current_parent:
                current_parent.remove_item(source_item)
            destination.add_item(source_item)
            return True
        return False

    def list_contents(self, folder_name: str) -> List[str]:
        folder = self._find_folder(folder_name, self.file_system)  
        if folder:
            return [item.get_name for item in folder.get_items]  
        return []

    def search_file_exact_match(self, folder_name: str, file_name: str) -> Optional[str]:
        folder = self._find_folder(folder_name, self.file_system)  
        if folder:
            for item in folder.get_items:  
                if not item.is_folder() and item.get_name.lower() == file_name.lower():
                    return item.get_name  # Return the original case
        return None

    def search_file_like_match(self, folder_name: str, pattern: str) -> List[str]:
        folder = self._find_folder(folder_name, self.file_system)  
        matches = []
        if folder:
            matches.extend(self._search_in_folder(folder, pattern.lower()))
        return matches

    def _search_in_folder(self, folder: Folder, pattern: str) -> List[str]:
        matches = []
        for item in folder.get_items:  
            if not item.is_folder() and pattern in item.get_name.lower():
                matches.append(item.get_name)
            elif item.is_folder():
                matches.extend(self._search_in_folder(item, pattern))
        return matches

    def list_directory_structure(self) -> str:
        return self._list_directory_structure_helper(self.file_system)

    def _list_directory_structure_helper(self, folder: Folder, prefix: str = "") -> str:
        structure = ""
        structure += "{}+ {}\n".format(prefix, folder.get_name)
        for item in folder.get_items:  
            if item.is_folder():
                structure += self._list_directory_structure_helper(item, prefix + "  ")  
            else:
                structure += "{}  - {}\n".format(prefix, item.get_name)  
        return structure

    def _find_folder(self, name: str, current_folder: Folder) -> Optional[Folder]:
        if current_folder.get_name.lower() == name.lower():
            return current_folder
        for item in current_folder.get_items:  
            if item.is_folder():
                result = self._find_folder(name, item)
                if result:
                    return result
        return None

    def _find_item(self, name: str, current_folder: Folder) -> Optional[File]:
        for item in current_folder.get_items:  
            if item.get_name.lower() == name.lower():
                return item
            if item.is_folder():
                found_item = self._find_item(name, item)
                if found_item:
                    return found_item
        return None

    def _find_parent(self, item: FileSystemItem) -> Optional[Folder]:
        return self._find_parent_helper(item, self.file_system)

    def _find_parent_helper(self, item: FileSystemItem, current_folder: Folder) -> Optional[Folder]:
        for child in current_folder.get_items:  
            if child is item:  
                return current_folder
            if child.is_folder():
                parent = self._find_parent_helper(item, child)
                if parent:
                    return parent
        return None