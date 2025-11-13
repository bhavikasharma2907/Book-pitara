print("welcome to my book pitara")
def run():
    print("press 1 for exit")
    print("press 2 for continue")
    
    a=int(input("Continue and Exit"))
    if a==1:
        pass
    elif a==2:
        print("Thanks for visiting")

    
    
def book():
    print("press 1 for book1: The diary of a young girl")
    print("press 2 for book2: Atomic habits")
    print("press 3 for book3: Attention")
    print("press 4 for book4: Psycology of humans")

    b=int(input("enter book number to continue"))
    if b==1:
        print("book1:--The Diary of a Young Girl, commonly referred to as The Diary of Anne Frank, is a book of the writings from the Dutch-language diary kept by Anne Frank while she was in hiding for two years with her family during the Nazi occupation of the Netherlands. The family was apprehended in 1944, and Anne Frank died of typhus in the Bergen-Belsen concentration camp in 1945. Anne's diaries were retrieved by Miep Gies and Bep Voskuijl. Miep gave them to Anne's father, Otto Frank, the family's only survivor, just after the Second World War was over.")

        run()
    elif b==2:
        print("book2:--At the turn of the twentieth century, Srinivasa Ramanujan is a struggling and indigent citizen in the city of Madras in India working at menial jobs at the edge of poverty. While performing his menial labour, his employers notice that he seems to have exceptional skills in mathematics and they begin to make use of him for rudimentary accounting tasks. It becomes equally clear to his employers, who are college-educated, that Ramanujan's mathematical insights exceed the simple accounting tasks they are assigning to him and soon they encourage him to make his personal writings in mathematics available to the general public and to start to contact professors of mathematics at universities by writing to them. One such letter is sent to G. H. Hardy, a famous mathematician at University of Cambridge, who begins to take a special interest in Ramanujan.")

        run()
    elif b==3:
        print("book3:--Attention or focus, is the concentration of awareness on some phenomenon to the exclusion of other stimuli.[1] It is the selective concentration on discrete information, either subjectively or objectively. William James (1890) wrote that Attention is the taking possession by the mind, in clear and vivid form, of one out of what seem several simultaneously possible objects or trains of thought. Focalization, concentration, of consciousness are of its essence Attention has also been described as the allocation of limited cognitive processing resources.[3] Attention is manifested by an attentional bottleneck, in terms of the amount of data the brain can process each second; for example, in human vision, less than 1% of the visual input data stream of 1MByte/sec can enter the bottleneck,[4][5] leading to inattentional blindness.")

        run()

    elif b==4:
        print("book4:--Psychology is the scientific study of behavior and mind.[1][2]z Its subject matter includes the behavior of humans and nonhumans, both conscious and unconscious phenomena, and mental processes such as thoughts, feelings, and motives. Psychology is an academic discipline of immense scope, crossing the boundaries between the natural and social sciences. Biological psychologists seek an understanding of the emergent properties of brains, linking the discipline to neuroscience. As social scientists, psychologists aim to understand the behavior of individuals and groups.")

        run()
    else:
        print("book not found")
        
book()
