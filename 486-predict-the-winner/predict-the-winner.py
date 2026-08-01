class Solution(object):
    def predictTheWinner(self, nums):
        def player1win(i ,j, p1_score, p2_score,is_pi_turn):
            if i >j:
                return p1_score >=p2_score

            if is_pi_turn:
                choose_left = player1win(i+1,j,p1_score+nums[i],p2_score,False)
                choose_right = player1win(i,j-1,p1_score+nums[j],p2_score,False)
                return choose_left or choose_right
            else:
                p2_chooses_left = player1win(i + 1, j, p1_score, p2_score + nums[i], True)
                p2_chooses_right = player1win(i, j - 1, p1_score, p2_score + nums[j], True)
                return p2_chooses_left and p2_chooses_right
        return player1win(0, len(nums) - 1, 0, 0, True)
        