import urllib2
def get_page(url):
    return urllib2.urlopen(url).read()

def get_next_target(page):
    start_link = page.find('details?id')
    if start_link == -1:
        return None, 0
    start_quote = page.find('=', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break

page = """                            </li>
                                                    <li id="gauge-534afd9846f84acc414a1835" class="collapsed gauge" data-id="534afd9846f84acc414a1835" data-gauge-type="spline">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=534afd9846f84acc414a1835" class="icon edit"></a>
                                        <a href="#" data-id="534afd9846f84acc414a1835" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="534afd9846f84acc414a1835" data-name="RMS Average Time to Acknowledgement">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/spline.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Average Time to Acknowledgement</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Trailing 30 days</span>
                                        </li>
                                        <li>
                                            Created on: April 13, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            Ticket Statistics&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-53712ce646f84aaf5ea83f8c" class="collapsed gauge" data-id="53712ce646f84aaf5ea83f8c" data-gauge-type="spline">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=53712ce646f84aaf5ea83f8c" class="icon edit"></a>
                                        <a href="#" data-id="53712ce646f84aaf5ea83f8c" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="53712ce646f84aaf5ea83f8c" data-name="RMS Average Time to Acknowledgement 6 Months">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/spline.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Average Time to Acknowledgement 6 Months</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Trailing 6 months</span>
                                        </li>
                                        <li>
                                            Created on: May 12, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            Ticket Statistics&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-534b6dba46f84a464019ffba" class="collapsed gauge" data-id="534b6dba46f84a464019ffba" data-gauge-type="spline">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=534b6dba46f84a464019ffba" class="icon edit"></a>
                                        <a href="#" data-id="534b6dba46f84a464019ffba" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="534b6dba46f84a464019ffba" data-name="RMS Average Time to Acknowledgement by Priority">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/spline.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Average Time to Acknowledgement by Priority</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Trailing 30 days</span>
                                        </li>
                                        <li>
                                            Created on: April 14, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            Ticket Statistics&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-53714d5646f84aac1aa89e09" class="collapsed gauge" data-id="53714d5646f84aac1aa89e09" data-gauge-type="spline">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=53714d5646f84aac1aa89e09" class="icon edit"></a>
                                        <a href="#" data-id="53714d5646f84aac1aa89e09" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="53714d5646f84aac1aa89e09" data-name="RMS Average Time to Acknowledgement by Priority 6 Months">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/spline.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Average Time to Acknowledgement by Priority 6 Months</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Trailing 6 Months</span>
                                        </li>
                                        <li>
                                            Created on: May 12, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            Ticket Statistics&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-534afe7046f84a27441ec2ed" class="collapsed gauge" data-id="534afe7046f84a27441ec2ed" data-gauge-type="spline">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=534afe7046f84a27441ec2ed" class="icon edit"></a>
                                        <a href="#" data-id="534afe7046f84a27441ec2ed" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="534afe7046f84a27441ec2ed" data-name="RMS Average Time to Resolution">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/spline.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Average Time to Resolution</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Trailing 30 days</span>
                                        </li>
                                        <li>
                                            Created on: April 13, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            Ticket Statistics&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-53714e7846f84a901a7c083f" class="collapsed gauge" data-id="53714e7846f84a901a7c083f" data-gauge-type="spline">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=53714e7846f84a901a7c083f" class="icon edit"></a>
                                        <a href="#" data-id="53714e7846f84a901a7c083f" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="53714e7846f84a901a7c083f" data-name="RMS Average Time to Resolution 6 Months">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/spline.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Average Time to Resolution 6 Months</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Trailing 6 Months</span>
                                        </li>
                                        <li>
                                            Created on: May 12, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            Ticket Statistics&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-534b6b4646f84a883d9f2e79" class="collapsed gauge" data-id="534b6b4646f84a883d9f2e79" data-gauge-type="spline">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=534b6b4646f84a883d9f2e79" class="icon edit"></a>
                                        <a href="#" data-id="534b6b4646f84a883d9f2e79" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="534b6b4646f84a883d9f2e79" data-name="RMS Opened vs. Closed Tickets">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/spline.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Opened vs. Closed Tickets</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Trailing 30 days</span>
                                        </li>
                                        <li>
                                            Created on: April 14, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            Opened vs. Closed Tickets&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-53714f1a46f84a4d1d4e1f0c" class="collapsed gauge" data-id="53714f1a46f84a4d1d4e1f0c" data-gauge-type="spline">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=53714f1a46f84a4d1d4e1f0c" class="icon edit"></a>
                                        <a href="#" data-id="53714f1a46f84a4d1d4e1f0c" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="53714f1a46f84a4d1d4e1f0c" data-name="RMS Opened vs. Closed Tickets 6 Months">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/spline.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Opened vs. Closed Tickets 6 Months</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Trailing 6 Months</span>
                                        </li>
                                        <li>
                                            Created on: May 12, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            Opened vs. Closed Tickets&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-534de47b46f84aca76e03675" class="collapsed gauge" data-id="534de47b46f84aca76e03675" data-gauge-type="table">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=534de47b46f84aca76e03675" class="icon edit"></a>
                                        <a href="#" data-id="534de47b46f84aca76e03675" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="534de47b46f84aca76e03675" data-name="RMS Remote Control Log">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/table.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Remote Control Log</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Trailing 30 days</span>
                                        </li>
                                        <li>
                                            Created on: April 16, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            Remote Control Log&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-53714fa046f84a981d32bd46" class="collapsed gauge" data-id="53714fa046f84a981d32bd46" data-gauge-type="table">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=53714fa046f84a981d32bd46" class="icon edit"></a>
                                        <a href="#" data-id="53714fa046f84a981d32bd46" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="53714fa046f84a981d32bd46" data-name="RMS Remote Control Log 6 Months">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/table.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Remote Control Log 6 Months</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Trailing 6 Months</span>
                                        </li>
                                        <li>
                                            Created on: May 12, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            Remote Control Log&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-534484c246f84a594d1623fa" class="collapsed gauge" data-id="534484c246f84a594d1623fa" data-gauge-type="table">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=534484c246f84a594d1623fa" class="icon edit"></a>
                                        <a href="#" data-id="534484c246f84a594d1623fa" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="534484c246f84a594d1623fa" data-name="RMS Server Disk Utilisation">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/table.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Server Disk Utilisation</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Real Time</span>
                                        </li>
                                        <li>
                                            Created on: April 08, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            Disk Statistics&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-534483e546f84a51508a2f80" class="collapsed gauge" data-id="534483e546f84a51508a2f80" data-gauge-type="table">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=534483e546f84a51508a2f80" class="icon edit"></a>
                                        <a href="#" data-id="534483e546f84a51508a2f80" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="534483e546f84a51508a2f80" data-name="RMS Server Inventory">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/table.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Server Inventory</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Real Time</span>
                                        </li>
                                        <li>
                                            Created on: April 08, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            Machine Statistics&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-536ac60946f84a200d998ecd" class="collapsed gauge" data-id="536ac60946f84a200d998ecd" data-gauge-type="table">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=536ac60946f84a200d998ecd" class="icon edit"></a>
                                        <a href="#" data-id="536ac60946f84a200d998ecd" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="536ac60946f84a200d998ecd" data-name="RMS Server Status">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/table.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Server Status</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Real Time</span>
                                        </li>
                                        <li>
                                            Created on: May 07, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            Machine Statistics&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-534b014f46f84a54467392db" class="collapsed gauge" data-id="534b014f46f84a54467392db" data-gauge-type="table">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=534b014f46f84a54467392db" class="icon edit"></a>
                                        <a href="#" data-id="534b014f46f84a54467392db" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="534b014f46f84a54467392db" data-name="RMS Ticket Summary">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/table.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Ticket Summary</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Trailing 30 days</span>
                                        </li>
                                        <li>
                                            Created on: April 13, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            *Ticket Stats Lite&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-537425d446f84abc0879b0c7" class="collapsed gauge" data-id="537425d446f84abc0879b0c7" data-gauge-type="table">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=537425d446f84abc0879b0c7" class="icon edit"></a>
                                        <a href="#" data-id="537425d446f84abc0879b0c7" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="537425d446f84abc0879b0c7" data-name="RMS Ticket Summary - Excluded Under Agreement">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/table.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Ticket Summary - Excluded Under Agreement</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Previous Month</span>
                                        </li>
                                        <li>
                                            Created on: May 15, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            Ticket Statistics&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-537421a046f84aa008b8911d" class="collapsed gauge" data-id="537421a046f84aa008b8911d" data-gauge-type="table">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=537421a046f84aa008b8911d" class="icon edit"></a>
                                        <a href="#" data-id="537421a046f84aa008b8911d" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="537421a046f84aa008b8911d" data-name="RMS Ticket Summary - Included Under Agreement">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/table.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Ticket Summary - Included Under Agreement</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Previous Month</span>
                                        </li>
                                        <li>
                                            Created on: May 15, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            Ticket Statistics&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-5371501346f84aa61db74f09" class="collapsed gauge" data-id="5371501346f84aa61db74f09" data-gauge-type="table">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=5371501346f84aa61db74f09" class="icon edit"></a>
                                        <a href="#" data-id="5371501346f84aa61db74f09" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="5371501346f84aa61db74f09" data-name="RMS Ticket Summary 6 Months">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/table.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Ticket Summary 6 Months</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Trailing 6 Months</span>
                                        </li>
                                        <li>
                                            Created on: May 12, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            *Ticket Stats Lite&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-534b72a546f84a5f453e11eb" class="collapsed gauge" data-id="534b72a546f84a5f453e11eb" data-gauge-type="pie">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=534b72a546f84a5f453e11eb" class="icon edit"></a>
                                        <a href="#" data-id="534b72a546f84a5f453e11eb" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="534b72a546f84a5f453e11eb" data-name="RMS Tickets Open by Priority">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/pie.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Tickets Open by Priority</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child"></span>
                                        </li>
                                        <li>
                                            Created on: April 14, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            *Currently Open Tickets&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-534b71ad46f84a58458a463f" class="collapsed gauge" data-id="534b71ad46f84a58458a463f" data-gauge-type="pie">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=534b71ad46f84a58458a463f" class="icon edit"></a>
                                        <a href="#" data-id="534b71ad46f84a58458a463f" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="534b71ad46f84a58458a463f" data-name="RMS Tickets Open by Status">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/pie.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Tickets Open by Status</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Currently Open</span>
                                        </li>
                                        <li>
                                            Created on: April 14, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            *Currently Open Tickets&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-534b705346f84ade44361e68" class="collapsed gauge" data-id="534b705346f84ade44361e68" data-gauge-type="pie">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=534b705346f84ade44361e68" class="icon edit"></a>
                                        <a href="#" data-id="534b705346f84ade44361e68" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="534b705346f84ade44361e68" data-name="RMS Tickets Opened by Type">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/pie.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Tickets Opened by Type</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Trailing 30 days</span>
                                        </li>
                                        <li>
                                            Created on: April 14, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            Ticket Statistics&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-534b04d346f84a224b3ba6ff" class="collapsed gauge" data-id="534b04d346f84a224b3ba6ff" data-gauge-type="column">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=534b04d346f84a224b3ba6ff" class="icon edit"></a>
                                        <a href="#" data-id="534b04d346f84a224b3ba6ff" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="534b04d346f84a224b3ba6ff" data-name="RMS Tickets Opened by Type and Sub-Type">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/column.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Tickets Opened by Type and Sub-Type</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Trailing 30 days</span>
                                        </li>
                                        <li>
                                            Created on: April 13, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            Ticket Statistics&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-5344862b46f84afb52fe6a67" class="collapsed gauge" data-id="5344862b46f84afb52fe6a67" data-gauge-type="table">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=5344862b46f84afb52fe6a67" class="icon edit"></a>
                                        <a href="#" data-id="5344862b46f84afb52fe6a67" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="5344862b46f84afb52fe6a67" data-name="RMS Workstation Disk Utilisation">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/table.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Workstation Disk Utilisation</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Real Time</span>
                                        </li>
                                        <li>
                                            Created on: April 08, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            Disk Statistics&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>
                            </li>
                                                    <li id="gauge-5344867646f84ac052238a97" class="collapsed gauge" data-id="5344867646f84ac052238a97" data-gauge-type="table">
                                <div class="last-child">
                                    <div class="actions">
                                        <a href="#" class="icon edit-in-builder"></a>
                                                                                <a href="/gauge/builder/details?id=5344867646f84ac052238a97" class="icon edit"></a>
                                        <a href="#" data-id="5344867646f84ac052238a97" class="icon delete"></a>
                                                                                <a href="#" class="clone last-child" data-id="5344867646f84ac052238a97" data-name="RMS Workstation Inventory">clone</a>
                                    </div>

                                    <img class="gauge-type" src="/static/imgs/gauges/types/thumbs/table.png">

                                    <ul class="info-list last-child">
                                        <li>
                                            <a href="#" class="gauge-title last-child">RMS Workstation Inventory</a>
                                        </li>
                                        <li>
                                            <span class="subtitle last-child">Real Time</span>
                                        </li>
                                        <li>
                                            Created on: April 08, 2014                                        </li>
                                        <li class="last-child">
                                            Dataset:
                                                                                                                                            Machine Statistics&nbsp;
                                                                                    </li>
                                    </ul>
                                </div>

"""
print_all_links(page)
