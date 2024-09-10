from XEdu.hub import Workflow as wf
model = wf(repo='yikshing/Mid-AutumnBlessings')
model.inference('Eason老师的中秋祝福小助手',port=7860)
