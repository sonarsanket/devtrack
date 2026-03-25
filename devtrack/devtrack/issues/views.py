import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reporter, Issue, CriticalIssue, LowPriorityIssue

REPORTER_FILE = "reporters.json"
ISSUE_FILE = "issues.json"


# ---------- COMMON FUNCTION ----------
def read_file(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return []


def save_file(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)


# ---------- REPORTER ----------
@api_view(['GET', 'POST'])
def reporters(request):

    data_list = read_file(REPORTER_FILE)

    # POST → Add reporter
    if request.method == "POST":
        try:
            r = Reporter(**request.data)
            r.validate()

            data_list.append(r.to_dict())
            save_file(REPORTER_FILE, data_list)

            return Response(r.to_dict(), status=201)

        except Exception as e:
            return Response({"error": str(e)}, status=400)

    # GET → Fetch reporter
    rid = request.GET.get("id")

    if rid:
        for r in data_list:
            if r["id"] == int(rid):
                return Response(r)
        return Response({"error": "Reporter not found"}, status=404)

    return Response(data_list)


# ---------- ISSUE ----------
@api_view(['GET', 'POST'])
def issues(request):

    data_list = read_file(ISSUE_FILE)

    # POST → Add issue
    if request.method == "POST":
        try:
            data = request.data

            # simple logic
            if data["priority"] == "critical":
                i = CriticalIssue(**data)
            elif data["priority"] == "low":
                i = LowPriorityIssue(**data)
            else:
                i = Issue(**data)

            i.validate()

            data_list.append(i.to_dict())
            save_file(ISSUE_FILE, data_list)

            res = i.to_dict()
            res["message"] = i.describe()

            return Response(res, status=201)

        except Exception as e:
            return Response({"error": str(e)}, status=400)

    # GET → Fetch issue
    iid = request.GET.get("id")
    status_filter = request.GET.get("status")

    if iid:
        for i in data_list:
            if i["id"] == int(iid):
                return Response(i)
        return Response({"error": "Issue not found"}, status=404)

    if status_filter:
        return Response([i for i in data_list if i["status"] == status_filter])

    return Response(data_list)