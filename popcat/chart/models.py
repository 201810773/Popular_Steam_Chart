from django.db import models
from datetime import datetime
from django.utils import timezone


class Game(models.Model):
    game_name = models.CharField(max_length=255)  # 게임 이름
    price = models.IntegerField(default=0)
    categories = models.CharField(max_length=1000, default="")  # 카데고리
    game_code = models.IntegerField(default=0)  # 게임 코드

    def __str__(self):
        return f"게임 이름:{self.game_name}"

    def get_categories_list(self):
        categories_set = set(
            category.strip()
            for category in self.categories.split(",")
            if category.strip()
        )
        return list(categories_set)


class TopSellers(models.Model):
    game = models.ForeignKey(
        Game, related_name="topsellers", on_delete=models.CASCADE
    )  # 게임 id
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # TopSellers에 올라와있던 해당 날짜
    game_code = models.IntegerField(default=0)  # 게임 코드

    def __str__(self):
        return f"게임 이름: {self.game.game_name} 생성 날짜:{self.created_at}"


class GameReviewers(models.Model):
    game = models.ForeignKey(
        Game, related_name="gamereviewers", on_delete=models.CASCADE
    )  # 게임 id
    pos_reviews = models.IntegerField(default=0)  # 긍정 리뷰어 수
    neg_reviews = models.IntegerField(default=0)  # 부정 리뷰어 수
    tot_reviews = models.IntegerField(default=0)  # 리뷰어 수 총합
    created_at = models.DateTimeField(default=timezone.now)
    game_code = models.IntegerField(default=0)  # 게임 코드

    def __str__(self):
        return f"게임 이름: {self.game.game_name} 리뷰어 수:{self.tot_reviews}"
