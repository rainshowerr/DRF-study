from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj): # 프로필 전체를 건드리지 않고 각 객체에 대한 요청만 있으므로 이 메소드를 가져옴
        if request.method in permissions.SAFE_METHODS: # SAFE_METHODS : GET과 같이 데이터에 영향을 미치지 않는 메소드
            return True
        return obj.user == request.user