from members import Member

class MemberRepository:
    def __init__(self):
        self.members = []

    def add_member(self, member: Member):
        self.members.append(member)
    
    def get_all_members(self):
        return self.members

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.id == member_id:
                return member
        return None

    def delete_member(self, member_id):
        member = self.find_member_by_id(member_id)
        if member:
            self.members.remove(member)
            return True
        return False
