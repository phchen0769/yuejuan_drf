# APIView
from rest_framework.views import APIView  # ⭐️核心视图类⭐️

# 用于处理所有HTTP请求的基本类，需要手动定义 get、post、put、delete 等方法。

# GenericAPIView
from rest_framework.generics import GenericAPIView  # ⭐️通用视图类⭐️

# 结合通用视图（Generic Views）和 API 视图的类，提供了用于处理数据库查询、序列化等任务的辅助方法。

# ListAPIView
from rest_framework.generics import ListAPIView  # ⭐️用于显示资源列表的通用视图⭐️

# 提供列出资源的功能，通常用于 HTTP GET 请求。

# CreateAPIView
from rest_framework.generics import CreateAPIView  # ⭐️用于创建资源的通用视图⭐️

# 提供创建资源的功能，通常用于 HTTP POST 请求。

# RetrieveAPIView
from rest_framework.generics import RetrieveAPIView  # ⭐️用于显示单个资源的通用视图⭐️

# 提供检索单个资源的功能，通常用于 HTTP GET 请求。

# UpdateAPIView
from rest_framework.generics import UpdateAPIView  # ⭐️用于更新资源的通用视图⭐️

# 提供更新资源的功能，通常用于 HTTP PUT 请求。

# DestroyAPIView
from rest_framework.generics import DestroyAPIView  # ⭐️用于删除资源的通用视图⭐️

# 提供删除资源的功能，通常用于 HTTP DELETE 请求。

# ListModelMixin
from rest_framework.mixins import ListModelMixin  # ⭐️提供列出资源的功能⭐️

# 用于在视图类中混合提供列出资源的功能。

# CreateModelMixin
from rest_framework.mixins import CreateModelMixin  # ⭐️提供创建资源的功能⭐️

# 用于在视图类中混合提供创建资源的功能。

# RetrieveModelMixin
from rest_framework.mixins import RetrieveModelMixin  # ⭐️提供检索资源的功能⭐️

# 用于在视图类中混合提供检索资源的功能。

# UpdateModelMixin
from rest_framework.mixins import UpdateModelMixin  # ⭐️提供更新资源的功能⭐️

# 用于在视图类中混合提供更新资源的功能。

# DestroyModelMixin
from rest_framework.mixins import DestroyModelMixin  # ⭐️提供删除资源的功能⭐️

# 用于在视图类中混合提供删除资源的功能。

# ViewSets
from rest_framework import viewsets  # ⭐️一种组织视图逻辑的方式⭐️

# 用于组织视图逻辑，提供对资源的常见操作的默认实现。

# ModelViewSet
from rest_framework import viewsets  # ⭐️提供了对模型资源进行增删改查的默认实现⭐️

# 用于在 ViewSets 中提供对模型资源进行增删改查的默认实现。

# ReadOnlyModelViewSet
from rest_framework import viewsets  # ⭐️提供对模型资源的只读操作的默认实现⭐️

# 用于在 ViewSets 中提供对模型资源的只读操作的默认实现。

# GenericViewSet
from rest_framework import viewsets  # ⭐️用于处理通用视图（Generic Views）的类⭐️

# 用于在 ViewSets 中处理通用视图（Generic Views）的类。
