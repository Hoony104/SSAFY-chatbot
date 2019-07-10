from flask import Flask, render_template
import requests
import random

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/Hi/<name>")
def Hi(name):
    return render_template('hello.html', name=name)

@app.route("/menu")
def menu():
    #랜덤 메뉴 추천, 해당음식 사진
    
    a={'짜장':'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAJYAyAMBIgACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAAEAAIDBQYHAQj/xAA+EAACAQMDAgMGAwYEBQUAAAABAgMABBEFEiExQQYTURQiYXGBkQcyoSNCscHR8BVScvEkM2KCohYlQ0Th/8QAGgEAAwEBAQEAAAAAAAAAAAAAAQIDAAQFBv/EACMRAAICAgIBBAMAAAAAAAAAAAABAhESIQMxQQQTUWEiMkL/2gAMAwEAAhEDEQA/ABNO8NX2qXAkmLzE/vufdX+laS5sdL8NJGCntF8oyobhQfU/0rfw2UUYUAk46DoBXKfF5ng1u/8Aat2Vl4LdNpAx9MUOSWCsbg485UTjULjUHe5upS6rgDJwMn0obzg28ISsgOeRwee2KE0ySS4sh5TRFS5DZPQ4zjH2qW5ikgHmF0jCsGLFhgV5Mueebo+gh6Tj9tKgxbeeNfMc47mmzX91EVe3WOdVXc0RbBZf+k/5v4/CrTTLGfV7JJXRbe173E2V3/6Aev2xUscWhaTtMNuL66H/AM84yAfgvQfrXTxe9L9ujz/U+xxqk9gVtHqd3re23tZZIITy4XCDKDjceOp9a0txDAkQF3eRRSA5HkrvZf5VR3mtXd2R5kzBR0UcAUCZiTkknPxqy9PDLJ9nI/WclUjUz63ZtbJAYHuVQ5DSnB/Shk1l14t7a3i+UYz9+aoVkz8KJifgcV0JnI3ey1fVr1+DO4+tRG7nbrK5PzNCK1SA0QEvmyHq5+9O81/85+9RinAVkayVZ3/zt96IjvZ1PEjfegwKetMYtoNUmUjLE/Wio9XkHWqVKlWiazQw6wjcOv1oyO9hk6HFZdDU6MR0o0HI0+4N0INKqCG5kj6OaOhv88SZ+dCg2WJNNPSo0lVx7pBPp3p2awSKQUqewpUAjtoPFU/iDQNP8QW/k6jBIZFGEmhO11+X9DWcOoXcn57iVvhvNFWQurqUJDK/HLMWICj1NB01RoycXcWVJ/Dq7sI3XStUjnDPv23UZjPwGRkHpTrXTLTRd8+rvDqGos27y0XEMJ9AP3sep+1W2sa0tnCbW1lkc9GkZiSax9xcNK5Zic1H2eOLtItL1fNKOLZYajq9zfvmV/dHRR2+VANJnAzQ5b414W5pzmJy3xpZ+ND7q9DUDBUZG7nmjYmHFV0JHrRcbYrIwahzUq0PE/rgfOpRMg6n7VrNROtO6DJOBUSzrn8pqSJzOSkcTu3cKM/wrWahjTADI5pLdYIyP1okaTet/wDUkUf9ZC/xNeHSb0cGFc9v2qZ+2a2aAexzqVz+lSpMpGc4oKaJrUDz8Id23BYHn04705cU6d9GaLBZV9aIjcHvVYoqeM4qqAWa808UJHNj81Eo+RRo1k8cjKcg4o2G6De7J9wearxzT1oNGstd425/d9RSoCGVo2zu+9KhQ1nONP1cX95Ha2CGWRmCj3ccn/Y/Y1qtUuk0qy9itzukxmaUcbmP8qpPw+02LSNA/wAal5nvI8QEptKxnv8ANsfbFC305uJndj3qMbS2PyNXSBZpC5JYkmhZGxTpnoVjWEHF6831EWpvmUA0EBqfnp6VFGd2B1z0ouWyaCMm9ube0jk92J5Jgp3fWkkzIaFdRuOFB6Z61orTwzqk9hDdW5gcSoHCM+GGex+nxqpuLOO1t4WW9R42RQZA2dxOOhHaujafYXltFHE19FJsUAARFf54qWcjNFfo+mez6bF7fpg9oLHdld/GTg556jFJ5tAE8trcx2kU6NtKTL5Rz8D3+dNbw87ODd69dFgckR5Gc9uSfWvR4c0Uw750mnjU5ZrqdnDfTPNTb3dg31Q248O282HtLiSFepUgSL9D/vRcWjiKLbJf3Xl91TEa/pVXquoecgtLawYWWMHdiOP4AAHJH6VmrnXNF0CfCaXoUjEkrFbQFpeO5YjaD07+oFBSUnsDdG0bTdKlYpmSST084Mf0qT/DNKAMQgUkHpH1B9CetcY13xnq1+5iMnlQA/8AIWMKn1A6/WorTVHkKNNpmkROnScRFXHyC9/rT0l4FyZ0bXr7TdNupIrzSNSithgrewAyJjHJIPTBzQ+n3yakC2iTQanEn50GYpkHrtJw36Vkf/UpiGJLu6cnqA7BT9CaVsn/AKgvVaw0tvOibm7aQwmM/wCtRx+po8fI70ZSbOm22m3M6K6RhQf8zgfpRS6RMv55YF/7s0Np/nwwRx3V0bsgbSyx8KO2XZssf4+lQakk0PmSw3QliGS8Mx2YH/S4/mK6HzTQ9IZDcwS3NxBbyCUW7BHkH5d2OQPlx96PhY4xmgLKKJLWL2WHyIgu5Yymwr8x60TDuPWumL1snYetSKaghwM54ogCmChwNKvBSoBspPE86RLHawKEjiUIiL0UAYAFZaU8GrbWZDLdyEngGqadgM96iwIEmOKDkkA71LM2c1VajdpawtI/J4CqOSTSsojzUL5LaEs7hR8TiqGz1O/ju47y6LNZXDGNSrKyg46cHhuOnXmgLjUDcXDvcQicFCqIXKiM+vHU0b4c1i70C5Go20FvLIv7BTOu4AYycUBja+HLfVtXuQ2labMyxgkS3QMMeeg5I5+mTWgtvwzv9QvBe+JNVV26CC3jGFX0yf6VR234m+KbhV2WUEvmbli8uE+8+OO/T4/CtLZa74le336h7NDMx92OOI7VHzyST9KlOWPgDlRb2n4c6Hboiut1OQ29Q9y6jd67UIHeidRuNWt2O1LZsDAIlZTj5EfzoPTNS1dri2ku7m2FsSRINvvsMEcenOKsGmld98EEsrDplOv3rn5JZregR/IC89rWH2nxBcQwL1W3jl3u3z6H7fesvr3j6QlYrCKMAHEYV92z0Ofyj9cVDrehavPqVxELV4435kmmbJbPOM+gzjAqCy8Jx2LCSbdLJ6kAAH4A5qKcYMntukZvUte1eWKWW6mnxKcIPe27R2Hw+IrOmd1fOx+DnPTmuty6bpKvjUZHaDcCwdxlhjv261Wxt4Ps3dv/AG8KSxwxDkbhyPtVY8v0ZwrtnO4HvJ5C0FnPOzc+5Gzk/YVo7LwX4m1HaDpi2qHvdzmPP03bvpitdcfiFo2nwhYDcXWQAI408tRgYHLY/QGqC6/FLWZzt0/T4LVe3WRvucfwp22+kHRc6T+FotlE2p38Ix1EUZXA/wBZO77YrQN/g+j2yRG7GyMd2CRrXLp9a8Uasze0XUiIeMNJ5YUfSvLXR7iRjNLetKyDJWFN5Hxy5xj5ZrVyMN0dU0/xNbXLBNLtmuP3faHBWIfEHq30+9Gal4n0vTrVhqF5Au5cPGoyx+gyea5HepFDG7XWpzJt90xPdkbvntx+lBJqmkQq3sdiHc/vyDCk/HPJqkYN9sGVm9l8fWtzfxQ+z+RaHGxpGGJDg8Mf3en9a0mna5pupJm2nVXzgo5w2f5/OuGXV1OJC6xp5bfmjaMCPj09D6ii4dQke3MEkEUIcYSVc+564HY4rpgseh8Ed8XOehqdW7VzDwn4t1BLr/D75hc+4CmWAYAdSD+8MfWugaXqMF8haIncnDIeoqimrpi4NFmOa9pueaVOKYvUDmR6qZxVtfj9q9Vkw61KjIqrlljUu5wo61iPEF+bi52xPhIzwQehrT+KZxDZ7c4Lk4+lYQHDE7QcnqT9an2y0dIO03TZLgeavlbOhL3EceOn+Y5+gGT2ptvC9/MYYTKoZ98cZbKIAMk//tR315Hv2WUDW8Cke4WyxbABLNj4fIVZ6c0EyyxWgIjJDt5r4YoMcZ9MkH6enFMY2fhTxfo2jGdZba8uriHbFFOAG93GSAWIIGT+ma2Phzx5pmu6lcwm3FlFbRh91yQTLu44wOAK4pMrQ30y2ytLHJjYQvI4B+9aj8PrKSS61C6b3IXiWP30JYsDn3fUDjPzqXLqLkuxZ/irOz/45o8KFxqdlGPUMMn6DmgJfGfh6OXf/iU88i90icj+A9ax1xpEB3MdSSGJW4dokU/qcVS3L6Eky26alc6hcu21YYGyWb0wo/vmuOPu8jvQqzZofEP4lKQy6fZuR3eZwg+3f71gtS8W6veFgLpoweMW6Ef+R/rWlk0K0toRJcvbWfGSuze/yyeB/ChItV0LTpHeGz9uIOBK2WGccc4wOc8d8U1Jve2ar0YoC7uGDsrysTgNIzOf0zRsWjahdQRC2srsOT7zqAikdB1IIrQXP4h3MMKeRaIsbdPLCoTjvjk+vXHSqDUvHmrXLYt0jhB6Ny7f0/SqxhP4CoMLtPDN2QWlgiQA4LSS8/YDkfWnu2jWDeXcXrXUvP8Aw+ngL067nOcfKszcXt7fq5vbm4lPQAvhM+mO56UDbuIJdyjdjoPSrKG9jYfZqJdc9siZdP062tGTlC+6Q7cHqSQF9eneqi/1TVbjInvJgn+VDtH/AI9frSjmguFVhGqv+Vtx6k/yp0t06KVWYqre8y54Pwp8UHFFckbO5ByuDhi3JogTtbzRNbny5ImDoyjkMOQfvUIUM7O7Ak5J5xnvTPMVpxwUXoCecf3xRQSyiu5EmdwmfM95g/vbyevXryT1om4kDgyokYt3H/LC/kIABGO/PIquPu+7J7rfGp4mDwTQNnDDcnOAGHSiYKWSS3tzGkjgsfc2PkoSOgIPHx7VeeFfEtzpt1HHKS652IxONvPQ+orPs8Nu6LHERtB37huPbj+NPE0U0kjgESdRg8H0PwpZRyQYuj6H028jvbVZkYE9GA7HuKVYf8OvEPtCxQyqcj9k5xgbieD8c9K8o8fMqqXYsuNp6LjV4zFeSL3JqonUDPr3rWeK7Xy5BMBwTyayswyT6U5DyZXxfFvs4yI2kaOQP5Yz769COPgaws/lyXTm0ieOJj7qO25l+Ge+K6H4qVhp00qEgqhAC9ecenNc9hmch09oMED8lhHneQeMfHnP3pPLLLpD5fKgthGw/atgsSBxn07njHpXlt5JkhWXcU3++FYKcfDPfr+lQCORl5ydw3MRyQ394p0UghuIbnylbD7vLwQNw7cfyotDJljLcpa6u7K7s8Q4CjJLnnbnJ45xn1qW9GpabbLI0rwPMu+WOOUjcrHIOOMYyB/OhbSCW5upbieJI0ywbd7oUsMDbk5LAnI+IGadrmpvqUyI8rSpDH5MLuuGKDnLfE9a1Kg9kd9PgQJNOl0BGHbGT5bHqpJ6sMDkcZNMgnnguxLZzvC8ZyJElKMoORwR069qDc+ZIqAqAT+8cCjRAsMaCZQz+X5nusPdHoSO/HSlSQX8Db3ULq/bfe3c9xIvP7ZyePl8KltZIMzbDKEII3DqeMjP1GMUPcSLcFAqqGUYyH/MPhn0FQx2pxuklCAnoAc/asBfRbWliyaqbaSFnKLu2Y4X1J74FBm0dJHMoChBl8HnnI6f7UVCtxFbSXxE/wCy2xrNuxyckAg84OCQfhT4tSWa1kgNwyLjdIQq5lxhR1GSfe6Zx1NHTDXkECRR3NvKq+YgdWKkYLcjijtYt1u9TmeGHMUaqrEHHPPNCuxZwYUZF35VepUdc0daSxTT6ql2doS2dsA8lgQBjPclh9M1OlkN/JW3Nu0Z2TnYUXaAV97occcZHbmpNPtXZ2ZYjLLEBvHp8KstJ08GUT6iZMcMoC8A+proOkaBDZeH7i9Eglnusshcg8HhfpQlLwBIy2laDql3EJ49MtpUxlYhKMuPr3oHU/C5vN403TbmK7Xh7doyMdeg/sVq9KkfQXRHNwsGQrKTu8vPwPat3p15HcvHwGc42sBz+tJlXQWfPQhmZvInh2yR+6RICu0js3cGomjkjkVPd2jB2oOD866X+OEUFtrunzwbPPmtm88D97a3ukn64rl5nkkuXJPpnjpgdq6ETDZGTO9n7cY9flUPnSW+2TornBBHPHemEywFo54cKwG4EAEfD1XPWnqFlQxSngDeod1XoMn3jgDgEfE4AyTRMXmga4NNlM8cStyN0bng46HivKz6JHvVUbhjjluB8zSqb4oydsbI+sNStEu7R42HvDgn0rnF/A9rcPFIuGU11e5XawcflPDVm/FGi+1xG4tgDKo5x1YVY55I5vqlot7ZSQMNyupyPWuVsTkxuvvRsRzyVxnIHpzXYVjdW2YIbmsf4i8Oeat/dW2faY5A4jA/OpA5++aSWh4Gf0ZFnWe3WSKIsgLM3DMueVX0J/lVde5WeaBLd1UZCIzlinvA5+wx8a8HmEq0aydcr2wRWt0vTLPTdN03WNStvNjlcrMG97KkHHB9MUHIejJi5kYCRmMmCRySfnz8a9tkE85QHaFG8nqcd/riunTeH/COs2v+IWXtYjmbeZAzKemNvI6cf0rLeLtN0+0tbJdKtmiiLPmRlOZiAOjnqR9ua17MUeoLZgxS2ayEbigLkHA7ZA746kcE54p7WqtbrvkiALZZ1JLtntjPb6Zz9ajFusVqfM5cAFQjbgoHXOOmRyPhUTuCdx5OAM/Ci3QUWd8mm200q2Nx5ijGyXydjcdicnj1+I4zyaK0fSLPUtMklk1e3trvJ8u0kB3SEHsegyB1z9Kot24e9g4HSvV4PujHHbj7/wB9qGQwfqftKWqRSXKyxr+ULJuUYPb70zTNFN6gmtmbPrjhe2KCMcsjYycHkljmui+DNGntrF4pi7Gch/KAz5fGPoSKnySpBRn7TQ97tGbhTtOGwMgkdqt7Tw1bRSBnt42OQdyjGMVu9P8AC7SqgeFYrYfmA4yPSp7nw3ctqKiGOOG0H5nRl5+G3t6Vz3LsbJdFFZWcDe6smCOD6irvUdMn1PS7S2sZmiZZo3LoRkquQR6dCalurORJhYWlqykj/mFcD6evzq3s7eHQLA+dJ5k8hzj1PoB2FLFu22CRiPEGhX1vrSJYpJc2zQ++Cy/s27YJ9euK0ehxR2sMcl9akTxH3CMN27Y79aPhDSsZWZHZzk5Gc1YpaR3cQ3wiOVTnCHr9qeLyFbo4F+Is9/f+KJ7jUbaSAFFW3QnIEY6c9Cecn51lQUgeJ2CyHOTHnjOehPy5+Rr6W1vR9A1iy9m1OBSgO9TvZGQ9NwPrzXKvH34bRaJYy6tolw81pDjzoZiC0ak43Kw689utdEJLoUwxtbhrYgLv2sMgHJBPc/1+FQzB4EXfHgEYAcdKNsbqRLaSBYYzuXaGZckc9jj4kVPLbtO0kp3+X+dZGIwD14B6j5dKr4NRo/w105bK+v7y7jjJgi8oKwVsMfeOOT2K/elV1+HenQvb2UKrIbiW69oZY3/ZxqAMllxg8hR88elKk2+jNxXZ3MgMpB70E37JvLcZQ/lJo+obpVZAG6npVUIY7xJoHvNeWakuOWQfxFYjU45ZY/OswPa4h+QnAkHp/T411tJGiby5enYnvVBr/htbgm5sSFl6lezUrQvXRxK109teurmS0tJIJID+3ZgVCN6H1PB4FbiLRIdV8KaRBduGjtJ1acYx5oUMu0/MkfTNX0dmI4JoSfKlkJLOFwS2AMn48AZ+FN0e1OlaettBFv2HhVP9fvXPOWLKJ2FQWEZt/atWaOCzgXMduxwoUd39B6L989KxfjnVLTxPp72tmoVLdg8UxQbeOwx+UYz1rdrAt6PI1URLvOUQPuGR0zkfmqs17S7+G3njEtulqF91grFmPptGAB9TmkTfaGOEmWWKOS3JwpOGUY97B/qBUMqbDtZSCBn+ddK8BeBDqmo3d7rti0enQgiKKQFRO574znaBz8yPSobnw3okGpXd5rF44tBKfJhlfChB6nqe/A/WrZrybE5usw3hVO4scYHJPyrS6V4Q1vUY1mEDWlseklwNu7twvU/pXRdF8RaBCAuj6ekSKMCRYliH0J5NWDa3a3l0sHtMZlkBPlo25iAMnn5UkuVIFMyek+EPZpVc77iUHhpMBE+n+9b/AEi2Wyg2nlu+P75qmv8AVNQVvZtPso8L1eRsnp2XgfrVpAWKguxZyOTiuaXIrsdLRbT6i0CkKAWx7qev9BXuiSahcxu144K5AVtm3Hr86Bgto9/mzEbB69/nR9peSXl1JCqMkEcYIkPRueg9KSEm5W2FpUHyXUUJ2qd7+tUl5dLdXgRk3FOMnv8AKo727jsh/wATKqFm2Ko43knpXlnbm4SRiSjk8MOoNLKbloKSWy3tYEJH7JV+lHsy28TLGpLnnjn61S2UF3Mvlm6AbuOh/Skyanp1ynBmjY8ZOQfhnt9aoptLoVqw+JIb+FoiwEsfI45Hxrm/4jazPaaXfaIsUkt5djaY0UvsiJzu4HQgYH1rpWposWy7h4kxgn1GM4NMiKahbQtdRKkoUkrngZ64Pcd8VaNXsU+a5dH1KHRYtXeMexM23dj8pzgZ+vFQ20tzqEqwtK5VFCoTyAM5/j2+NdM/GO81OSzXTv8ACprTTIpAz3XDJN1x+X8oBOecc1T/AIaeE7/VXjutvs1kDue4Ye8464Qdh/farpugpo3n4e6FcaJY+Zegefcrln35x6Lz/eaVbNI1UKqcIg2rn5Y/hSq0XSOeat2XWaEvnwVAokmgL9/2oHwopDkTOsi7HPPY15HM0TbXGRUBODTTIQMNyppwImvNOtr9NxGH7MvWqS5srmyuFcR5jJw+3t8atUleI5Q5X0ouK6jlG04+RqPJxKQejC63ZzzTSzxSOyEDbHn8nGOMfHmtZbWghsY7WSV5ljQL5jtlzgdc1NcaXbzEumFb9Kz99FrVrqVuvswfTydrvG5JGehx6f3muRwlx7qx00wDxR4gvT5ujeF7R3uIwFmupIm8mD1AY9W+OfvVd4O8KXEkN02vOt9NLIp8xk4AIwVHbHA6etXF7Dfyapb2lkkbLMMu5PIUHn9O9aa8Ahsnig3BmQqGHVcjGftQUn2xm/COLaV4OFhOZHuY51Vj7jp27cn6VtdM8MaVqEtrfac4tLy1lDP5YGG9Q6dwRkZ681WXPh5fDuoLfW8D3FhIqxzhMlo2zw2PTsa1FtpWmTNFdW1vJFKnIZHYGlyt2Fk9/oE83v2c8UUoGMtyD86Ymi6qI1X2y1VhjLbCwP0q2uBKYA8Dsj9xnrWe1TUL2OFzFcys2PdjTAJqcsYvaCrLhNKtrfEt/O07ryNzbEH/AGjrROnzRSuzQgBAowcVi7bVNqq2oSYkJwGds8/HNajw9PFObgwspxt3BTnrn0rQlclSBJaK+/0G4vb6R5fJMUjHJds4GegFW8sK2FkI4vffhQW79ia8W7xJIoYDBI6VG77z7il27k8ZpU4rrsNtrYFJbSXHia1MAKsbdzLIvGPeGB+prUYQqYXO87AWJHWotNtngjLXAQXEn5wvIX0AqJVZLqWWQ4yT1PQevyxVorBW/IrdkF/ceYZYx1jB4Hc/CmWAePTElmjKXLoCY2OfLY9Fz8O+Pjiuf3Wr6rqXie51DTciyVREispKugP5j8c5x862mmTtqcsE1u4MMBPmcdyMbfnRVtgejzTb+8FoYdbSBpRw5iGFb5qeBVjFc+YUEKFLfH5wOvwUfzpS6THJqBu53ygUAQnpnuT/AH2p9zf21mhbIyBgetdcON+STd9BA/LmUbF7etKsnqevTygiH9nHnrnmlVaBTN+TVdqBPnf9orylTBBM5NOAHzpUqICJ0KcqcVESf3eGHcUqVZhJIrySMgdasLe78xcsufnXlKlYxL5EMj+YE2yYxuA7elRtbyR73WQOvoygEfClSqU4R+BbYwS+9gDBPcU5kYrnd3xzSpVzSHQJcSNEQc5BNVGs2UIkScKMynB+frXtKuaW7sZGbvtD9qv7OYyAICTJgkMVAPFbDSbO00vTZZ4IFjDe++wctgdz3NKlW41saRBZWrTBZWk2xs24gLkkVfRWtvCAyx89ieTSpVXgiqsEmRz3kUcmNrFwM/Cm3lob5FCyGLkFsc5FKlV4pPsnLREum2kK++hm/wBfT7Uy41FLSNViiCqOiqAAKVKupRS6Qidmevtdncsq5VRVHNdyysWLH6mlSojMFlkZuSc0qVKgE//Z',
       '짬뽕':'data:image/jpeg;base64,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'}
    mlist=list(a.keys())
    smenu=random.choice(mlist)
    simage=a.get(smenu)
    # a={'짜장':'1번', '짬뽕':'2번'}
    # b=random.choice(list(a.keys()))
    # print(b)
    # c=a.get(b)
    # print(c)
    return render_template('menu.html',smenu=smenu, simage=simage)

    ##menus=[, , , ]
    ##menu=random.choice(menus)
    ##images={ : , : , : , : }
    ##image=images[choice]

@app.route("/lottery")
def lottery():
    url='https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'
    scratch=requests.get(url).json()
    win=[]
    for i in range(6):
        win.append(scratch[f'drwtNo{i+1}'])
    sug=sorted(random.sample(range(1,46),6))

    pri=len(set(win)&set(sug))
    if pri==6:
        result='1등'
    elif pri>=3:
        result=f'{8-pri}등'
    else:
        result='꽝!'

    return render_template('lottery.html', sug=sug, result=result)

        

if __name__ == "__main__":
    app.run(debug=True)